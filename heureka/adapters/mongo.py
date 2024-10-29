import json
import logging

import motor.motor_asyncio
from pydantic import BaseModel

from heureka.merger.model import Offer, Product
from heureka.merger.ports import Repository

log = logging.getLogger(__name__)

class MongoConfig(BaseModel):
    host: str
    port: int
    user: str
    password: str
    database: str

class MongoAdapter(Repository):

    COLLECTION = "products"

    def __init__(self, config: MongoConfig) -> None:
        self.database = config.database
        self.client = motor.motor_asyncio.AsyncIOMotorClient(
            host=config.host,
            port=config.port,
            username=config.user,
            password=config.password,
        )
        self.db = self.client[self.database]


    async def save(self, product: Product) -> None:
        await self.db[self.COLLECTION].update_one(
            {"ids": str(next(iter(product.ids)))},
            {"$set": json.loads(product.model_dump_json())},
            upsert=True)

    async def load_by_offer(self, offer: Offer) -> Product | None:
        ret = await self.db[self.COLLECTION].find_one({"ids": str(offer.id)})
        return Product.model_validate(ret) if ret else None

