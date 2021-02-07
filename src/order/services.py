import sys
sys.path.insert(0, '/Users/temi/cosmic-code/code/src/order')
from domain import model
from repository import AbstractRepository, FakeRepository


def create_portfolio(reference: str, ticker: str,name: str,qty: int,price: float, repo: AbstractRepository):
    data = repo.get() 
    asset  = model.Asset(ticker,name,qty, price)
    holding = model.Holding(asset)
    if reference  is not data:
        _portfolio = model.create_portfolio(reference,[holding])
        _return_portfolio = repo.add(_portfolio)
        repo.commit()
        return _return_portfolio

def retrieve_portfolio(reference:str, repo: AbstractRepository):
    data = repo.list()
    for _portfolio in data:
        if _portfolio.id == reference:
            repo.commit
            return _portfolio

def add_holding_to_portfolio(reference: str, new_holding: model.Holding, repo: AbstractRepository):
    all_portfolio = repo.list()
    updated_portfolio = model.add_portfolio_holding(reference,new_holding,all_portfolio)
    repo.commit()
    return updated_portfolio

def delete_portfolio_holding(reference: str, delete_holding: model.Holding, repo: AbstractRepository):
    all_portfolio = repo.list()
    updated_portfolio = model.delete_portfolio_holding(reference,delete_holding,all_portfolio)
    repo.commit()
    return updated_portfolio 

