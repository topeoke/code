from __future__ import annotations
from dataclasses import dataclass, replace
from typing import List, Optional
from datetime import date


@dataclass
class Asset:
    ticker: str
    name: str
    qty: int
    price: float
    currency: str = "GBP"
    asset_type: str = "Equity"
    total: float = 0.00


class Holdings:
    def __init__(
        self, asset_entry: Asset
    ):
        self.asset_entry = asset_entry
        self._holdings = set()

    def isAssetValid(self) -> bool:
        return self.asset_entry.qty > 0 and self.asset_entry.price > 0
    
    @property
    def assetHoldings(self):
        if self.isAssetValid():
            self.asset_entry.total = self.asset_entry.qty * self.asset_entry.price
            return self.asset_entry
            

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













