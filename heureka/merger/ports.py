from abc import ABC, abstractmethod
from uuid import UUID

from heureka.merger.model import Offer, Product


class Repository(ABC):
    @abstractmethod
    async def save(self, product: Product) -> None:
        pass

    @abstractmethod
    async def load_by_offer(self, offer: Offer) -> Product | None:
        pass


class Matching(ABC):
    @abstractmethod
    async def match(self, offer: Offer) -> set[UUID]:
        pass

class ErrorReporter(ABC):
    @abstractmethod
    def repository_error(self, offer: Offer, error: "RepositoryException") -> None:
        pass

    @abstractmethod
    def matching_error(self, offer: Offer, error: "MatchingException") -> None:
        pass


class RepositoryException(Exception):
    pass


class MatchingException(Exception):
    pass