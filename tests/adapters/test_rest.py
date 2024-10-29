from uuid import UUID

import pytest

from heureka.adapters.rest import RestAdapter, MatchingConfig
from heureka.merger.model import Offer


@pytest.fixture
def adapter() -> RestAdapter:
    return RestAdapter(
        config=MatchingConfig(
            url="http://localhost:5555/offer-matches",
            auth="827e8e1a-119c-48e2-af1c-cef81f933a5a"
        )
    )

@pytest.mark.parametrize(
    "offer_id,matched_ids",
    [
        ("00000000-00000000-00000000-00000000", set()),

        ("0a10d511-6a65-444d-9628-3c6993ba7dbd", {"0a10d511-6a65-444d-9628-3c6993ba7dbd"}),

        ("631aa5a8-9b5d-4ae2-945a-00a0a539b101", {"631aa5a8-9b5d-4ae2-945a-00a0a539b101", "38495bd1-afe9-4cd0-bf9d-eca162e75542", "feaa400a-d304-4f55-b045-51b1daec8e0c"}),
        ("38495bd1-afe9-4cd0-bf9d-eca162e75542", {"631aa5a8-9b5d-4ae2-945a-00a0a539b101", "38495bd1-afe9-4cd0-bf9d-eca162e75542", "feaa400a-d304-4f55-b045-51b1daec8e0c"}),
        ("feaa400a-d304-4f55-b045-51b1daec8e0c", {"631aa5a8-9b5d-4ae2-945a-00a0a539b101", "38495bd1-afe9-4cd0-bf9d-eca162e75542", "feaa400a-d304-4f55-b045-51b1daec8e0c"}),

        ("29e0b669-a670-476b-808a-e21a449d1c0f", {"29e0b669-a670-476b-808a-e21a449d1c0f", "ed87340d-3703-45b1-a7f8-5fa7d22fc9e9"}),
        ("ed87340d-3703-45b1-a7f8-5fa7d22fc9e9", {"29e0b669-a670-476b-808a-e21a449d1c0f", "ed87340d-3703-45b1-a7f8-5fa7d22fc9e9"}),
    ]
)
@pytest.mark.asyncio
async def test_match_no_match(adapter: RestAdapter, offer_id: str, matched_ids) -> None:
    matching = await adapter.match(offer=Offer(
        id=UUID(offer_id),
        category="cat",
        name="name",
        description="desc",
        parameters={"param": "value"}
    ))
    assert matching == matched_ids
