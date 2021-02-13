import sys
sys.path.insert(0, '/Users/temi/cosmic-code/code/src/order')
from domain import model
from adapters.repository import AbstractRepository, FakeRepository
from service_layer.unit_of_work import AbstractUnitOfWork


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

def add_portfolio_asset(reference, asset: model.Asset, repo: AbstractRepository):
    all_portfolio = repo.list()
    updated_portfolio = model.add_portfolio_asset(reference, asset, all_portfolio)
    repo.commit()
    return updated_portfolio

def create_portfolio_uow(reference: str, ticker: str,name: str,qty: int,price: float, uow: AbstractUnitOfWork):
    asset  = model.Asset(ticker,name,qty, price)
    holding = model.Holding(asset)
    with uow:
        data = uow.portfolio.get()
        print(data)
        if reference  is not data:
            _portfolio = model.create_portfolio(reference,[holding])
            print(_portfolio)
            _return_portfolio = uow.portfolio.add(_portfolio)
            return _return_portfolio

def add_holding_to_portfolio_uow(reference: str, new_holding: model.Holding, uow: AbstractUnitOfWork):
    with uow:
        all_portfolio = uow.portfolio.list()
        print(all_portfolio)
        updated_portfolio = model.add_portfolio_holding(reference,new_holding,all_portfolio)
        print(updated_portfolio)
        uow.portfolio.commit()
        return updated_portfolio

def add_portfolio_asset_uow(reference, asset: model.Asset, uow: AbstractUnitOfWork):
    with uow:
        all_portfolio = uow.portfolio.list()
        updated_portfolio = model.add_portfolio_asset(reference, asset, all_portfolio)
        uow.portfolio.commit()
        return updated_portfolio
    
def delete_portfolio_holding_uow(reference: str, delete_holding: model.Holding, uow: AbstractUnitOfWork):
    with uow:
        all_portfolio = uow.portfolio.list()
        updated_portfolio = model.delete_portfolio_holding(reference,delete_holding,all_portfolio)
        uow.portfolio.commit()
        return updated_portfolio 