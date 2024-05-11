from dataclasses import dataclass
from enum import Enum


class OrderType(Enum):
    MARKET = "Market"
    LIMIT = "Limit"


@dataclass
class StockOrder:
    symbol: str
    quantity: int
    order_type: OrderType
    price: float = 0.0
