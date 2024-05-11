from src.utils.data_types import OptionOrder, OptionType, OrderType, StockOrder


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
    
    def test_option_type(self):
        assert OptionType.CALL.value == "Call"
        assert OptionType.PUT.value == "Put"

    def test_option_order(self):
        order = OptionOrder("AAPL", "2021-01-01", OptionType.CALL, 150.0, OrderType.MARKET)
        assert order.sym == "AAPL"
        assert order.expiration == "2021-01-01"
        assert order.option_type == OptionType.CALL
        assert order.strike == 150.0
        assert order.order_type == OrderType.MARKET