from dataclasses import dataclass
import attr
from typing import List, Optional
from datetime import date


@dataclass(frozen=True)
class Asset:
    ticker: str
    name: str
    qty: int
    price: float
    total: float

@attr.s
class Portfolio(object):
    id: int = attr.ib()
    holdings: set() = attr.ib()
    total: float = attr.ib()
    date_created: Optional[date] = attr.ib()
    date_updated: Optional[date] = attr.ib()









