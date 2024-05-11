from src.utils.data_types import OrderType, StockOrder


class TestDataTypes:
    def test_order_type(self):
        assert OrderType.MARKET.value == "Market"
        assert OrderType.LIMIT.value == "Limit"
    
    def test_stock_order(self):
        order = StockOrder("AAPL", 100, OrderType.MARKET)
        assert order.symbol == "AAPL"
        assert order.quantity == 100
        assert order.order_type == OrderType.MARKET
        assert order.price == 0.0

        order2 = StockOrder("AAPL", 100, OrderType.LIMIT, 150.0)
        assert order2.symbol == "AAPL"
        assert order2.quantity == 100
        assert order2.order_type == OrderType.LIMIT
        assert order2.price == 150.0