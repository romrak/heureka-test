import logging

from heureka.merger.model import Offer
from heureka.merger.ports import ErrorReporter, RepositoryException, MatchingException

logger = logging.getLogger(__name__)

class StdReporter(ErrorReporter):
    def repository_error(self, offer: Offer, error: RepositoryException) -> None:
        logger.error(f"Failed to process offer: {offer}: {error}")

    def matching_error(self, offer: Offer, error: MatchingException) -> None:
        logger.error(f"Failed to process offer: {offer}: {error}")
