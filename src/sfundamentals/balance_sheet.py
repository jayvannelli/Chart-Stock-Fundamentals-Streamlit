import streamlit as st
from streamlit.errors import StreamlitAPIException
import pandas as pd
from .base import StreamlitFundamentals
from fundamentals.containers import BalanceSheetsContainer


class StreamlitBalanceSheets(StreamlitFundamentals):
    """Plot IncomeStatementsContainer objects using streamlit."""

    def __init__(self, data: BalanceSheetsContainer) -> None:
        """Initialize Streamlit component to plot fundamentals Income Statements.

        Parameter
        ---------
        data : IncomeStatementsContainer
            FundamentalsFactory or StockFundamentalsFactory response from fundamentals.
        """
        if not isinstance(data, BalanceSheetsContainer):
            raise IOError("data must be an IncomeStatementsContainer.")

        self.data = data

    @property
    def symbol(self):
        return self.data.symbol

    @property
    def period(self):
        return self.data.period

    @property
    def limit(self):
        return self.data.limit

    def get_data(self):
        """Returns list of IncomeStatement objects."""
        return self.data.balance_sheets

    def valid_values(self):
        """Returns valid values for 'value' param in chart method calls."""
        from ._constants import VALID_BALANCE_SHEET_VALUES

        return VALID_BALANCE_SHEET_VALUES

    def chart_single_value(self, value: str):
        """Plots one value in Income Statement over time.

        Parameter
        ---------
        value : str
            Income statement value to plot.
        """
        if value not in self.valid_values():
            raise ValueError(
                f"Invalid income statement value: {value}. "
                f"To get valid values call the 'valid_values' func."
            )

        _values = [
            balance_sheet.__getattribute__(value) for balance_sheet in self.data.balance_sheets
        ]
        _indexes = [
            balance_sheet.date for balance_sheet in self.data.balance_sheets
        ]

        data = {value: _values}

        try:
            st.bar_chart(
                data=pd.DataFrame(data, index=_indexes),
            )

        except StreamlitAPIException:
            raise StreamlitAPIException

    def chart_multiple_values(self, values: list[str]):
        """Plots multiple values in Income Statement over time.

        Parameter
        ---------
        values : list[str]
            Income statement values to plot (maximum = 5).
        """
        _values_data = {}

        if len(values) > 5:
            raise ValueError(
                "values cannot contain more than 5 elements."
            )

        for value in values:
            if value not in self.valid_values():
                raise ValueError(
                    f"Invalid income statement value: {value}. "
                    f"To get valid values call the 'valid_values' func."
                )

            value_data = [
                balance_sheet.__getattribute__(value) for balance_sheet in self.data.balance_sheets
            ]
            _values_data[value] = value_data

        _indexes = [
            balance_sheet.date for balance_sheet in self.data.balance_sheets
        ]

        try:
            st.bar_chart(
                data=pd.DataFrame(_values_data, _indexes),
            )

        except StreamlitAPIException:
            raise StreamlitAPIException
