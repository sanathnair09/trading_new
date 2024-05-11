from pathlib import Path
from brokers.broker_abc import Broker
from src.utils.data_types import OptionOrder, StockOrder


class Fidelity(Broker):
    def __init__(self, equity_report_file: Path, option_report_file: Path) -> None:
        super().__init__(equity_report_file, option_report_file)

    def name(self) -> str:
        raise NotImplementedError

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

    def _market_buy(self, order: StockOrder) -> str | dict | None:
        raise NotImplementedError

    def _market_sell(self, order: StockOrder) -> str | dict | None:
        raise NotImplementedError

    def _limit_buy(self, order: StockOrder) -> str | dict | None:
        raise NotImplementedError

    def _limit_sell(self, order: StockOrder) -> str | dict | None:
        raise NotImplementedError

    def _buy_call_option(self, order: OptionOrder) -> str | dict | None:
        raise NotImplementedError

    def _sell_call_option(self, order: OptionOrder) -> str | dict | None:
        raise NotImplementedError

    def _buy_put_option(self, order: OptionOrder) -> str | dict | None:
        raise NotImplementedError

    def _sell_put_option(self, order: OptionOrder) -> str | dict | None:
        raise NotImplementedError
