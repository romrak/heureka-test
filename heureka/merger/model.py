from typing import Any
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class Offer(BaseModel):
    model_config = ConfigDict(frozen=True)

    id: UUID
    category: str
    name: str
    description: str
    parameters: dict[str, Any]


class Diff(BaseModel):
    model_config = ConfigDict(frozen=True)

    common: int
    differ: int

class OfferParameters(BaseModel):
    model_config = ConfigDict(frozen=True)

    parameters: dict[str, Any]
    diff: Diff

class Product(BaseModel):
    model_config = ConfigDict(frozen=True, extra='ignore')

    ids: set[UUID]
    parameters: dict[str, set[Any]]
    offers: dict[UUID, OfferParameters]
