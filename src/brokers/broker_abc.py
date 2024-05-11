from abc import ABC, abstractmethod
from pathlib import Path


class Broker(ABC):
    def __init__(self, equity_report_file: Path, option_report_file: Path) -> None:
        self._equity_report_file = equity_report_file
        self._option_report_file = option_report_file
    
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError
    

    
