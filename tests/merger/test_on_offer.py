import json
import uuid
from pathlib import Path
from typing import Any
from unittest.mock import Mock

import pytest

from heureka.merger.merger import Merger
from heureka.merger.model import Offer, Product
from heureka.merger.ports import RepositoryException, Repository, ErrorReporter, Matching, MatchingException

ids = [uuid.uuid4() for _ in range(5)]

@pytest.fixture
def offer() -> Offer:
    return Offer(
        id=uuid.uuid4(),
        category="cat",
        name="name",
        description="desc",
        parameters={"param": "value"}
    )


@pytest.fixture
def repository_exception() -> RepositoryException:
    return RepositoryException()

@pytest.fixture
def matching_exception() -> MatchingException:
    return MatchingException()

@pytest.fixture
def failing_repository(mocker: Any, repository_exception: RepositoryException) -> Mock:
    repository = mocker.Mock(spec=Repository)
    repository.load_by_offer.side_effect = repository_exception
    return repository

@pytest.fixture
def failing_matching(mocker: Any, matching_exception: MatchingException) -> Mock:
    matching = mocker.Mock(spec=Matching)
    matching.match.side_effect = matching_exception
    return matching


@pytest.fixture
def repository() -> Mock:
    return Mock(spec=Repository)

@pytest.fixture
def matching() -> Mock:
    return Mock(spec=Matching)


@pytest.fixture
def reporter(mocker) -> Mock:
    return mocker.Mock(spec=ErrorReporter)

@pytest.fixture
def merger_with_failing_repository(failing_repository: Mock, matching: Mock, reporter: Mock) -> Merger:
    return Merger(
        repository=failing_repository,
        matching=matching,
        reporter=reporter
    )

@pytest.fixture
def merger_with_failing_matching(repository: Mock, failing_matching: Mock, reporter: Mock) -> Merger:
    return Merger(
        repository=repository,
        matching=failing_matching,
        reporter=reporter
    )

@pytest.fixture
def merger(repository: Mock, matching: Mock, reporter: Mock) -> Merger:
    return Merger(
        repository=repository,
        matching=matching,
        reporter=reporter
    )

@pytest.mark.asyncio
async def test_on_repository_exception_reports_error(
        offer: Offer,
        merger_with_failing_repository: Merger,
        reporter: Mock,
        repository_exception: RepositoryException) -> None:
    await merger_with_failing_repository.on_offer(offer)

    reporter.repository_error.assert_called_once_with(offer, repository_exception)

@pytest.mark.asyncio
async def test_on_repository_exception_returns_false(offer: Offer, merger_with_failing_repository: Merger) -> None:
    assert await merger_with_failing_repository.on_offer(offer) is False


@pytest.mark.asyncio
async def test_on_matching_exception_reports_error(
        offer: Offer,
        merger_with_failing_matching: Merger,
        reporter: Mock,
        matching_exception: MatchingException) -> None:
    await merger_with_failing_matching.on_offer(offer)

    reporter.matching_error.assert_called_once_with(offer, matching_exception)

@pytest.mark.asyncio
async def test_on_matching_exception_returns_false(offer: Offer, merger_with_failing_matching: Merger) -> None:
    assert await merger_with_failing_matching.on_offer(offer) is False


def _read_scenarios() -> list[pytest.param]:
    scenarios = Path(Path(__file__).parent, "scenarios").glob("*.json")
    for scenario in scenarios:
        with open(scenario) as f:
            raw = json.load(f)
            print(raw)
            yield pytest.param(
                Offer(**raw["offer"]),
                Product(**raw["repository_product"]) if raw["repository_product"] else None,
                set(raw["matching_list"]),
                Product(**raw["expected_product"]),
                id=f.name
            )

@pytest.mark.parametrize(
    "offer,repository_product,matching_list,expected_product",
    _read_scenarios()
)
@pytest.mark.asyncio
async def test_scenarios(
        merger: Merger,
        repository: Mock,
        matching: Mock,

        offer: Offer,
        repository_product: Product,
        matching_list: list[uuid.UUID],
        expected_product: Product,
) -> None:
    repository.load_by_offer.return_value = repository_product
    matching.match.return_value = matching_list

    assert await merger.on_offer(offer) is True

    # to see nice json for debug
    print(expected_product.model_dump_json(indent=4))
    print(repository.save.call_args[0][0].model_dump_json(indent=4))

    repository.save.assert_called_once_with(expected_product)
