from abc import ABC, abstractmethod


class StreamlitFundamentals(ABC):
    """Interface for streamlit fundamentals child classes."""

    @abstractmethod
    def __init__(self):
        ...

    @abstractmethod
    def symbol(self):
        ...

    @abstractmethod
    def period(self):
        ...

    @abstractmethod
    def limit(self):
        ...

    @abstractmethod
    def get_data(self):
        ...

    @abstractmethod
    def valid_values(self):
        ...

    @abstractmethod
    def chart_single_value(self, value: str):
        ...

    @abstractmethod
    def chart_multiple_values(self, values: list[str]):
        ...
