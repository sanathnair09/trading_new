from pathlib import Path
import time
from src.brokers.broker_abc import Broker
from src.constants import FIDELITY_LOGIN, FIDELITY_PASSWORD
from src.utils.data_types import BrokerNames, OptionOrder, StockOrder
from src.utils.selenium_wrapper import CustomChromeInstance
from selenium.webdriver.common.by import By


class Fidelity(Broker):
    def __init__(self, equity_report_file: Path, option_report_file: Path) -> None:
        super().__init__(equity_report_file, option_report_file)
        self._webdriver = CustomChromeInstance()
        self._webdriver.open(
            "https://digital.fidelity.com/prgw/digital/login/full-page"
        )

    def name(self) -> str:
        return BrokerNames.FD.value

    def login(self) -> None:
        login_input_elem = self._webdriver.find(
            By.XPATH, '//*[@id="dom-username-input"]'
        )
        self._webdriver.sendKeyboardInput(login_input_elem, FIDELITY_LOGIN)
        time.sleep(1)
        password_input_elem = self._webdriver.find(
            By.XPATH, '//*[@id="dom-pswd-input"]'
        )
        self._webdriver.sendKeyboardInput(password_input_elem, FIDELITY_PASSWORD)
        time.sleep(1)
        login_button = self._webdriver.find(By.XPATH, '//*[@id="dom-login-button"]')
        login_button.click()
        time.sleep(5)  # will have to play with time depending on your internet speeds
        self._webdriver.open(
            "https://digital.fidelity.com/ftgw/digital/trade-equity/index/orderEntry"
        )

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


if __name__ == "__main__":
    fidelity = Fidelity(Path(""), Path(""))
    fidelity.login()
