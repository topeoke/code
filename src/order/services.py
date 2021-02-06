import sys
sys.path.insert(0, '/Users/temi/cosmic-code/code/src/order')
from domain import model
from repository import AbstractRepository, FakeRepository


def create_portfolio(reference: str, ticker: str,name: str,qty: int,price: float, repo: AbstractRepository):
    data = repo.get() 
    asset  = model.Asset(ticker,name,qty, price)
    holding = model.Holding(asset)
    if reference not in data:
        _portfolio = model.create_portfolio(reference,[holding])
        _return_portfolio = repo.add(_portfolio)
        repo.commit()
        return _return_portfolio
