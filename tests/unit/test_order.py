import sys
sys.path.insert(0, '/Users/temi/cosmic-code/code/src')
from order.domain.model import Asset, Portfolio, Holdings
from datetime import date, time

def create_asset():
    new_asset = Asset(ticker = "abc", name="abc", qty = 10, price = 10.34)
    return new_asset

def test_asset_is_created():
    new_asset = Asset(ticker = "abc", name="abc", qty = 10, price = 10.34)
    assert new_asset.name == "abc"
    assert new_asset.ticker == "abc"
    assert new_asset.qty == 10

def create_portfolio():
    all_holdings = list()
    new_asset = Asset(ticker = "abc", name="abc", qty = 10, price = 10.34)
    new_asset_2 = Asset(ticker = "abcb", name="abcb", qty = 50, price = 145.34)
    new_asset_3 = Asset(ticker = "cde", name="cde", qty = 500, price = 56.34)
    all_holdings.append(new_asset)
    all_holdings.append(new_asset_2)
    all_holdings.append(new_asset_3)
    return all_holdings

def test_portfolio_is_created():
    all_holdings = create_portfolio()
    new_portfolio = Portfolio(id = 100, holdings=all_holdings, date_created=date, date_updated=date)
    assert new_portfolio.holdings == all_holdings

def test_portfolio_total():
    all_holdings = create_portfolio()
    total = sum(item.qty * item.price for item in all_holdings)
    new_portfolio = Portfolio(id = 100, holdings=all_holdings, date_created=date, date_updated=date)
    assert new_portfolio.total == total

def test_asset_holding_is_valid():
    test_asset = create_asset()
    new_asset = Asset(ticker = "abc", name="abc", qty = 20, price = 10.34)
    holding = Holdings(test_asset)
    assert holding.isAssetValid() == True


def test_asset_holding_allocation():
    test_asset  = create_asset()
    holding = Holdings(test_asset)
    assert holding.assetHoldings == test_asset
 