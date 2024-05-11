from abc import ABC, abstractmethod
from pathlib import Path

from utils.data_types import OptionOrder, StockOrder

OrderResult = str | dict | None


class Broker(ABC):
    def __init__(self, equity_report_file: Path, option_report_file: Path) -> None:
        self._equity_report_file = equity_report_file
        self._option_report_file = option_report_file

    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def login(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def buy(self, order: StockOrder) -> None:
        raise NotImplementedError

    @abstractmethod
    def sell(self, order: StockOrder) -> None:
        raise NotImplementedError

    @abstractmethod
    def buy_option(self, order: OptionOrder) -> None:
        raise NotImplementedError

    @abstractmethod
    def sell_option(self, order: OptionOrder) -> None:
        raise NotImplementedError

    @abstractmethod
    def _market_buy(self, order: StockOrder) -> OrderResult:
        raise NotImplementedError

    @abstractmethod
    def _market_sell(self, order: StockOrder) -> OrderResult:
        raise NotImplementedError

    @abstractmethod
    def _limit_buy(self, order: StockOrder) -> OrderResult:
        raise NotImplementedError

    @abstractmethod
    def _limit_sell(self, order: StockOrder) -> OrderResult:
        raise NotImplementedError

    @abstractmethod
    def _buy_call_option(self, order: OptionOrder) -> OrderResult:
        raise NotImplementedError

    @abstractmethod
    def _sell_call_option(self, order: OptionOrder) -> OrderResult:
        raise NotImplementedError

    @abstractmethod
    def _buy_put_option(self, order: OptionOrder) -> OrderResult:
        raise NotImplementedError

    @abstractmethod
    def _sell_put_option(self, order: OptionOrder) -> OrderResult:
        raise NotImplementedError
