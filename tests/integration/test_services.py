import pytest
import sys
sys.path.insert(0, '/Users/temi/cosmic-code/code/src')
from order.domain.model import Asset, Portfolio, Holding
from order.service_layer.services import create_portfolio, retrieve_portfolio, add_holding_to_portfolio, delete_portfolio_holding
from order.service_layer.services import add_portfolio_asset, create_portfolio_uow,add_holding_to_portfolio_uow
from order.service_layer.services import add_portfolio_asset_uow, delete_portfolio_holding_uow
from order.service_layer.unit_of_work import FakeUnitOfWork
from order.adapters.repository import FakeRepository
from datetime import date, time

def create_holdings():
    all_holdings = list()
    new_asset = Asset(ticker = "abc", name="abc", qty = 10, price = 10.34)
    new_asset_2 =  Asset(ticker = "abcb", name="abcb", qty = 50, price = 145.34)
    new_asset_3 = Asset(ticker = "cde", name="cde", qty = 500, price = 56.34)
    all_holdings.append(Holding(new_asset).assetHoldings)
    all_holdings.append(Holding(new_asset_2).assetHoldings)
    all_holdings.append(Holding(new_asset_3).assetHoldings)
    return all_holdings


def test_create_portfolio_service():
    all_holdings = create_holdings()
    repo = FakeRepository([Portfolio('234',all_holdings, date, date)])
    _result = create_portfolio('123', 'IBM', 'Intl_Bus_Machine', 100, 10.23, repo )
    assert _result == '123'


def test_retrieve_portfolio_service():
    all_holdings = create_holdings()
    repo = FakeRepository([Portfolio('234',all_holdings, date, date)])
    _result = retrieve_portfolio('234', repo)
    assert _result.holdings == all_holdings

def test_add_holding_to_portfolio_service():
    all_holdings = create_holdings()
    repo = FakeRepository([Portfolio('234',all_holdings, date, date)])
    new_asset_4 = Asset(ticker = "xyz", name="xyz plc", qty = 1500, price = 156.34)
    new_holding = Holding(new_asset_4).assetHoldings
    res = add_holding_to_portfolio('234', new_holding, repo)
    assert res.holdings == all_holdings

def test_delete_portfolio_holding():
    all_holdings = create_holdings()
    repo = FakeRepository([Portfolio('234',all_holdings, date, date)])
    delete_asset = Asset(ticker = "cde", name="cde", qty = 500, price = 56.34)
    delete_holding = Holding(delete_asset).assetHoldings
    res =  delete_portfolio_holding('234', delete_holding, repo)
    assert res.holdings == all_holdings

def test_update_portfolio_asset():
    all_holdings = create_holdings()
    repo = FakeRepository([Portfolio('234',all_holdings, date, date)])
    add_asset = Asset(ticker = "cde", name="cde", qty = 700, price = 56.34)
    port_asset_add = add_portfolio_asset('234', add_asset, repo)
    assert port_asset_add.holdings == all_holdings

def test_create_portfolio_service_uow():
    all_holdings = create_holdings()
    f_uow = FakeUnitOfWork([])
    _result = create_portfolio_uow('123', 'IBM', 'Intl_Bus_Machine', 100, 10.23, f_uow )
    assert _result == '123'

def test_add_holding_to_portfolio_service_uow():
    all_holdings = create_holdings()
    fake_uow = FakeUnitOfWork([Portfolio('234',all_holdings, date, date)])
    new_asset_4 = Asset(ticker = "xyz", name="xyz plc", qty = 1500, price = 156.34)
    new_holding = Holding(new_asset_4).assetHoldings
    res = add_holding_to_portfolio_uow('234', new_holding, fake_uow)
    assert res.holdings == all_holdings

def test_update_portfolio_asset_uow():
    all_holdings = create_holdings()
    fake_uow = FakeUnitOfWork([Portfolio('234',all_holdings, date, date)])
    #repo = FakeRepository([Portfolio('234',all_holdings, date, date)])
    add_asset = Asset(ticker = "cde", name="cde", qty = 700, price = 56.34)
    port_asset_add = add_portfolio_asset_uow('234', add_asset, fake_uow)
    assert port_asset_add.holdings == all_holdings

def test_delete_portfolio_holding_uow():
    all_holdings = create_holdings()
    fake_uow = FakeUnitOfWork([Portfolio('234',all_holdings, date, date)])
    delete_asset = Asset(ticker = "cde", name="cde", qty = 500, price = 56.34)
    delete_holding = Holding(delete_asset).assetHoldings
    res =  delete_portfolio_holding_uow('234', delete_holding, fake_uow)
    assert res.holdings == all_holdings