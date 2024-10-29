import asyncio
import logging
import sys

from heureka.adapters.mongo import MongoAdapter, MongoConfig
from heureka.adapters.rabbit import RabbitClient, RabbitConfig
from heureka.adapters.rest import RestAdapter, MatchingConfig
from heureka.merger.merger import Merger

logging.basicConfig(format="%(asctime)s %(levelname)-8s %(message)s", stream=sys.stdout, level=logging.INFO)

async def main() -> None:

    repository = MongoAdapter(config=MongoConfig(
        host="localhost",
        port=27017,
        user="root",
        password="example",
        collection="products"
    ))

    matching = RestAdapter(config=MatchingConfig(
        url="http://localhost:5555/offer-matches",
        auth="827e8e1a-119c-48e2-af1c-cef81f933a5a"
    ))

    merger = Merger(repository=repository, matching=matching, reporter=None)

    rabbit_client = RabbitClient(
        config=RabbitConfig(
            host="localhost",
            virtual_host="/",
            login="guest",
            password="guest",
            port=5672,
            max_message_count=66,
            exchange_name="amq.topic",
        ),
        merger=merger
    )
    await rabbit_client.start()

if __name__ == '__main__':
    asyncio.run(main())
