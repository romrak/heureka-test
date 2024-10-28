from uuid import UUID

from heureka.merger.model import Offer, Product


class Repository:
    async def save(self, product: Product) -> None:
        pass

    async def load_by_offer(self, offer: Offer) -> Product | None:
        pass


class Matching:
    async def match(self, offer: Offer) -> set[UUID]:
        pass

class ErrorReporter:
    def repository_error(self, offer: Offer, error: "RepositoryException") -> None:
        pass

    def matching_error(self, offer: Offer, error: "MatchingException") -> None:
        pass


class RepositoryException(Exception):
    pass


class MatchingException(Exception):
    pass