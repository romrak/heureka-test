import json
import uuid

import pytest
from pymongo import MongoClient

from heureka.adapters.mongo import MongoAdapter, MongoConfig
from heureka.merger.model import OfferParameters, Diff, Product, Offer


@pytest.fixture
def collection() -> str:
    return "test-collection"

@pytest.fixture
def database() -> str:
    return "test-db"

@pytest.fixture
def adapter(collection: str, database: str) -> MongoAdapter:
    return MongoAdapter(
        config=MongoConfig(
            host="localhost",
            port=27017,
            user="root",
            password="example",
            collection=collection,
            database=database
        )
    )

@pytest.fixture
def client() -> MongoClient:
    return MongoClient(
        host="localhost",
        port=27017,
        username="root",
        password="example"
    )

@pytest.mark.asyncio
async def test_save(client: MongoClient, adapter: MongoAdapter, collection: str, database: str) -> None:
    client[database][collection].delete_many({})
    cursor = client[database][collection].find()
    assert len(cursor.to_list()) == 0

    offer_id = uuid.uuid4()
    product = Product(
        ids={offer_id},
        parameters= {"param": {"value"}},
        offers={
            offer_id: OfferParameters(
                parameters={"param": "value"},
                diff=Diff(common=1, differ=0)
            )
        }
    )

    await adapter.save(product)

    cursor = client[database][collection].find()
    saved = cursor.to_list()
    assert len(saved) == 1

    saved_product = Product.model_validate(saved[0])

    assert saved_product == product


@pytest.mark.asyncio
async def test_load_by_offer(client: MongoClient, adapter: MongoAdapter, collection: str, database: str) -> None:
    client[database][collection].delete_many({})
    cursor = client[database][collection].find()
    assert len(cursor.to_list()) == 0

    offer_id = uuid.uuid4()
    product = Product(
        ids={offer_id},
        parameters= {"param": {"value"}},
        offers={
            offer_id: OfferParameters(
                parameters={"param": "value"},
                diff=Diff(common=1, differ=0)
            )
        }
    )

    client[database][collection].insert_one(json.loads(product.model_dump_json()))
    cursor = client[database][collection].find()
    assert len(cursor.to_list()) == 1

    offer = Offer(
        id=offer_id,
        category="cat",
        name="name",
        description="desc",
        parameters={"param": "value"}
    )

    loaded_product = await adapter.load_by_offer(offer)
    assert product == loaded_product