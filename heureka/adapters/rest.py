import urllib.parse
from uuid import UUID

import requests
from pydantic import BaseModel

from heureka.merger.model import Offer
from heureka.merger.ports import Matching, MatchingException


class MatchingConfig(BaseModel):
    url: str
    auth: str

class RestAdapter(Matching):

    def __init__(self, config: MatchingConfig):
        self.config = config

    async def match(self, offer: Offer) -> set[UUID]:
        response = requests.get(
            f"{self.config.url}/{urllib.parse.quote(str(offer.id))}",
            headers={
                "Auth": self.config.auth
            })
        if response.status_code == 404:
            return set()
        if response.status_code == 200:
            try:
                return set(response.json().get("matching_offers", []))
            except Exception as e:
                raise MatchingException(e)