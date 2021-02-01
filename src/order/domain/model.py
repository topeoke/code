from __future__ import annotations
from dataclasses import dataclass
from typing import List, Optional
from datetime import date


@dataclass(frozen=True)
class Asset:
    ticker: str
    name: str
    qty: int
    price: float
    currency: str = "GBP"


class Portfolio:
    def __init__(
        self, id: str, holdings: set(), date_created: Optional[date], date_updated: Optional[date] ,
        total=  0.0):
        self.id = id
        self.holdings = holdings
        self.date_created = date_created
        self.date_updated = date_updated


    def __repr__(self):
        return self.id

    @property
    def total(self) -> int:
        return sum(asset.qty * asset.price for asset in self.holdings)











