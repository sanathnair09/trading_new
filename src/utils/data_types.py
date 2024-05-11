from dataclasses import dataclass
from enum import Enum


class BrokerNames(Enum):
    RH = "RH"  # Robinhood
    E2 = "E2"  # ETrade
    SB = "SB"  # Schwab
    FD = "FD"  # Fidelity
    IF = "IF"  # IBKR free
    VD = "VD"  # Vanguard

class OrderType(Enum):
    MARKET = "Market"
    LIMIT = "Limit"

class OptionType(Enum):
    CALL = "Call"
    PUT = "Put"


@dataclass
class StockOrder:
    symbol: str
    quantity: int
    order_type: OrderType = OrderType.MARKET
    price: float | str = 0.0


@dataclass
class OptionOrder:
    sym: str
    expiration: str
    option_type: OptionType
    strike: float | str
    order_type: OrderType = OrderType.MARKET