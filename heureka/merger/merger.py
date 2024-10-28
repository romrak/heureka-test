from typing import Any
from uuid import UUID

from heureka.merger.model import Offer, Product, OfferParameters, Diff
from heureka.merger.ports import Repository, ErrorReporter, RepositoryException, Matching, MatchingException


class Merger:
    def __init__(self, *, repository: Repository, matching: Matching, reporter: ErrorReporter):
        self.repository = repository
        self.matching = matching
        self.reporter = reporter

    async def on_offer(self, offer: Offer) -> bool:
        try:
            product_coro = self.repository.load_by_offer(offer)
            match_coro = self.matching.match(offer)
            current_product = await product_coro
            matching = await match_coro
            if not current_product:
                await self.repository.save(self._new_product(offer, matching))
            else:
                await self.repository.save(self._merge_product(offer, current_product, matching))

            return True
        except RepositoryException as e:
            self.reporter.repository_error(offer, e)
            return False
        except MatchingException as e:
            self.reporter.matching_error(offer, e)
            return False

    def _new_product(self, offer: Offer, matching: set[UUID]) -> Product:
        return Product(
            ids=matching or {offer.id},
            parameters={key: {value} for key, value in offer.parameters.items()},
            offers={
                offer.id: OfferParameters(
                    parameters=offer.parameters,
                    diff=Diff(
                        common=len(offer.parameters),
                        differ=0
                    ))
            }
        )

    def _merge_product(self, offer: Offer, product: Product, matching: set[UUID]) -> Product:
        merged_parameters = self._merge_parameters(offer, product)
        return Product(
            ids=matching,
            parameters=merged_parameters,
            offers=self._update_offers(offer, product, merged_parameters)
        )

    def _merge_parameters(self, offer: Offer, product: Product) -> dict[str, set[Any]]:
        parameters = {
            key: {value} for key, value in offer.parameters.items()
        }

        for offer_id, product_offer in product.offers.items():
            if offer_id != offer.id:
                for key, value in product_offer.parameters.items():
                    if key in parameters:
                        parameters[key].add(value)
                    else:
                        parameters[key] = {value}
        return parameters

    def _update_offers(self, offer: Offer, product: Product, merged_parameters: dict[str, set[str]]) -> dict[UUID, OfferParameters]:
        offers = {
            offer.id: OfferParameters(
                parameters=offer.parameters,
                diff=self._diff(merged_parameters, offer.parameters)
        )}
        for offer_id, product_offer in product.offers.items():
            if offer_id != offer.id:
                offers[offer_id] = OfferParameters(
                    parameters=product_offer.parameters,
                    diff=self._diff(merged_parameters, product_offer.parameters)
                )
        return offers

    def _diff(self, parameters: dict[str, set[Any]], offer_parameters: dict[str, Any]) -> Diff:
        common = 0
        differ = 0
        for key, value in parameters.items():
            if key in offer_parameters and value == {offer_parameters[key]}:
                common += 1
            else:
                differ += 1
        return Diff(common=common, differ=differ)