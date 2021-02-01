import sys
sys.path.insert(0, '/Users/temi/cosmic-code/code/src')
from order.domain.model import Asset, Portfolio
from datetime import date, time

def test_asset_is_created():
    new_asset = Asset(ticker = "abc", name="abc", qty = 10, price = 10.34, total = 102.5)
    assert new_asset.name == "abc"
    assert new_asset.ticker == "abc"
    assert new_asset.qty == 10

def test_portfolio_is_created():
    all_holdings = list()
    new_asset = Asset(ticker = "abc", name="abc", qty = 10, price = 10.34, total = 102.5)
    new_asset_2 = Asset(ticker = "abcb", name="abcb", qty = 50, price = 145.34, total = 102.5)
    all_holdings.append(new_asset)
    all_holdings.append(new_asset_2)
    new_portfolio = Portfolio(id=34, holdings=all_holdings, total = 100.00, date_created=date, date_updated=date)
    assert new_portfolio.holdings == all_holdings
    assert new_portfolio.holdings[0].total == 102.5
    for item in all_holdings:
        assert new_portfolio.holdings[all_holdings.index(item)].total == item.total