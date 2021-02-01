import sys
sys.path.insert(0, '/Users/temi/cosmic-code/code/src')
from order.domain.model import Asset, Portfolio

def test_asset_is_created():
    new_asset = Asset(ticker = "abc", name="abc", qty = 10, price = 10.34, total = 102.5)
    assert new_asset.name == "abc"
    assert new_asset.ticker == "abc"
    assert new_asset.qty == 10


def test_portfolio_is_created():
    