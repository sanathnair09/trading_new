from pathlib import Path
import pytest
from src.brokers.broker_abc import Broker, OrderResult
from src.utils.data_types import OptionOrder, StockOrder


class TestBrokerAbc:
    @pytest.fixture
    def concrete_broker(self):
        class ConcreteBroker(Broker):
            def name(self) -> str:
                return "ConcreteBroker"

            def login(self) -> None:
                raise NotImplementedError

            def buy(self, order: StockOrder) -> None:
                raise NotImplementedError

            def sell(self, order: StockOrder) -> None:
                raise NotImplementedError

            def buy_option(self, order: OptionOrder) -> None:
                raise NotImplementedError

            def sell_option(self, order: OptionOrder) -> None:
                raise NotImplementedError

            def _market_buy(self, order: StockOrder) -> OrderResult:
                raise NotImplementedError

            def _market_sell(self, order: StockOrder) -> OrderResult:
                raise NotImplementedError

            def _limit_buy(self, order: StockOrder) -> OrderResult:
                raise NotImplementedError

            def _limit_sell(self, order: StockOrder) -> OrderResult:
                raise NotImplementedError

            def _buy_call_option(self, order: OptionOrder) -> OrderResult:
                raise NotImplementedError

            def _sell_call_option(self, order: OptionOrder) -> OrderResult:
                raise NotImplementedError

            def _buy_put_option(self, order: OptionOrder) -> OrderResult:
                raise NotImplementedError

            def _sell_put_option(self, order: OptionOrder) -> OrderResult:
                raise NotImplementedError

        return ConcreteBroker(Path(""), Path(""))

    def test_broker_abc_init(self, concrete_broker):
        assert concrete_broker._equity_report_file == Path("")
        assert concrete_broker._option_report_file == Path("")

    def test_broker_abc_name(self, concrete_broker):
        assert concrete_broker.name() == "ConcreteBroker"
