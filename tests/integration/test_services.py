import pytest
import sys
sys.path.insert(0, '/Users/temi/cosmic-code/code/src')
from order.domain.model import Asset, Portfolio, Holding
from order.services import create_portfolio, retrieve_portfolio, add_holding_to_portfolio
from order.repository import FakeRepository
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
    assert res.holdings == all_holdings, all_holdings.total
