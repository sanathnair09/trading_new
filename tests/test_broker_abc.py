from pathlib import Path
import pytest
from src.brokers.broker_abc import Broker


class TestBrokerAbc:
    @pytest.fixture
    def concrete_broker(self):
        class ConcreteBroker(Broker):
            def name(self) -> str:
                return "ConcreteBroker"
        return ConcreteBroker(Path(""), Path(""))
            
    def test_broker_abc_init(self, concrete_broker):
        assert concrete_broker._equity_report_file == Path("")
        assert concrete_broker._option_report_file == Path("")

    def test_broker_abc_name(self, concrete_broker):
        assert concrete_broker.name() == "ConcreteBroker"