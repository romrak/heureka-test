import asyncio
import logging
import os
import sys

from heureka.adapters.mongo import MongoAdapter, MongoConfig
from heureka.adapters.rabbit import RabbitClient, RabbitConfig
from heureka.adapters.rest import RestAdapter, MatchingConfig
from heureka.adapters.stdreporter import StdReporter
from heureka.merger.merger import Merger

logging.basicConfig(format="%(asctime)s %(levelname)-8s %(message)s", stream=sys.stdout, level=logging.INFO)

async def main() -> None:

    repository = MongoAdapter(config=MongoConfig(
        host=os.environ.get("MONGO_HOST"),
        port=int(os.environ.get("MONGO_PORT")),
        user=os.environ.get("MONGO_USER"),
        password=os.environ.get("MONGO_PASSWORD"),
        database=os.environ.get("MONGO_DATABASE")
    ))

    matching = RestAdapter(config=MatchingConfig(
        url=os.environ.get("MATCHING_URL"),
        auth=os.environ.get("MATCHING_AUTH"),
    ))

    reporter = StdReporter()

    merger = Merger(repository=repository, matching=matching, reporter=reporter)

    rabbit_client = RabbitClient(
        config=RabbitConfig(
            host=os.environ.get("RABBITMQ_HOST"),
            virtual_host=os.environ.get("RABBITMQ_VIRTUAL_HOST"),
            login=os.environ.get("RABBITMQ_LOGIN"),
            password=os.environ.get("RABBITMQ_PASSWORD"),
            port=int(os.environ.get("RABBITMQ_PORT")),
            max_message_count=int(os.environ.get("MESSAGES_COUNT")),
            exchange_name=os.environ.get("RABBITMQ_EXCHANGE_NAME"),
        ),
        merger=merger
    )
    await rabbit_client.start()

if __name__ == '__main__':
    asyncio.run(main())
