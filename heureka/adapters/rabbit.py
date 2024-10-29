import asyncio
import logging

import aio_pika
import aiormq
from aio_pika.abc import AbstractRobustConnection
from pydantic import BaseModel, ValidationError

from heureka.merger.merger import Merger
from heureka.merger.model import Offer

log = logging.getLogger(__name__)


class RmqOffer(BaseModel):
    metadata: dict[str, str]
    payload: Offer

class RabbitConfig(BaseModel):
    host: str
    virtual_host: str
    login: str
    password: str
    port: int

    max_message_count: int
    exchange_name: str

class RabbitClient:
    def __init__(self, config: RabbitConfig, merger: Merger) -> None:
        self.config = config
        self.merger = merger

    async def start(self) -> None:
        log.info("Connecting to RabbitMQ")
        connection = await self._connect()
        log.info("Connected to RabbitMQ")

        channel = await connection.channel()
        await channel.set_qos(prefetch_count=self.config.max_message_count)
        queue = await channel.declare_queue("product_offer", auto_delete=True)
        exchange = await channel.get_exchange(self.config.exchange_name)
        await queue.bind(exchange, routing_key="oc.offer")
        log.info("Bound queue to exchange")

        await queue.consume(self._process_message)

        try:
            # Wait until terminate
            await asyncio.Future()
        finally:
            await connection.close()


    async def _connect(self) -> AbstractRobustConnection:
        while True:
            try:
                return await aio_pika.connect_robust(
                    host=self.config.host,
                    port=self.config.port,
                    virtualhost=self.config.virtual_host,
                    login=self.config.login,
                    password=self.config.password,
                )
            except aiormq.exceptions.AMQPConnectionError:
                log.info("Failed to connect to RabbitMQ, retrying in 1 second")
                await asyncio.sleep(1)

    async def _process_message(self, message: aio_pika.abc.AbstractIncomingMessage) -> None:
        async with message.process():
            try:
                offer = RmqOffer.model_validate_json(message.body)
                await self.merger.on_offer(offer.payload)
            except ValidationError as e:
                log.error(f"Invalid offer: {e}")
