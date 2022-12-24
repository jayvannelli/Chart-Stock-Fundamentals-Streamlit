import streamlit as st
from streamlit.errors import StreamlitAPIException
import pandas as pd
from .base import StreamlitFundamentals
from fundamentals.containers import CashFlowsContainer


class StreamlitCashFlows(StreamlitFundamentals):
    """Plot CashFlowsContainer objects using streamlit."""

    def __init__(self, data: CashFlowsContainer) -> None:
        """Initialize Streamlit component to plot fundamentals Cash Flows.

        Parameter
        ---------
        data : CashFlowsContainer
            FundamentalsFactory or StockFundamentalsFactory response from fundamentals.
        """
        if not isinstance(data, CashFlowsContainer):
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
        """Returns list of CashFlow objects."""
        return self.data.cash_flows

    def valid_values(self):
        """Returns valid values for 'value' param in chart method calls."""
        from ._constants import VALID_CASH_FLOW_VALUES

        return VALID_CASH_FLOW_VALUES

    def chart_single_value(self, value: str):
        """Plots one value in Cash Flows over time.

        Parameter
        ---------
        value : str
            Cash flow value to plot.
        """
        if value not in self.valid_values():
            raise ValueError(
                f"Invalid income statement value: {value}. "
                f"To get valid values call the 'valid_values' func."
            )

        _values = [
            cash_flow.__getattribute__(value) for cash_flow in self.data.cash_flows
        ]
        _indexes = [
            cash_flow.date for cash_flow in self.data.cash_flows
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
            Cash flow values to plot (maximum = 5).
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
                cash_flow.__getattribute__(value) for cash_flow in self.data.cash_flows
            ]
            _values_data[value] = value_data

        _indexes = [
            cash_flow.date for cash_flow in self.data.cash_flows
        ]

        try:
            st.bar_chart(
                data=pd.DataFrame(_values_data, _indexes),
            )

        except StreamlitAPIException:
            raise StreamlitAPIException
