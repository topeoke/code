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
    asset_type: str = "Equity"

class Holdings:
    def __init__(
        self
    ):
        self._holdings = set()

    def isAssetValid(self, asset_entry: Asset) -> bool:
        return asset_entry.qty > 0 and asset_entry.price > 0
    
    def assetHoldings(self, asset_entry: Asset):
        if self.isAssetValid(asset_entry):
            return self._holdings.add(asset_entry)

    @property
    def test(self):
        return self._holdings

class Portfolio:
    def __init__(
        self, id: str, holdings: List[Asset], date_created: Optional[date], date_updated: Optional[date] ,
        total=  0.0):
        self.id = id
        self.holdings = holdings
        self.date_created = date_created
        self.date_updated = date_updated


    def __repr__(self):
        return self.id

    @property
    def total(self) -> float:
        return sum(asset.qty * asset.price for asset in self.holdings)













