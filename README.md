# Streamlit Component to py-fundamentals

You must use the factory classes in py-fundamentals to use this
package.

Streamlit must be in use already (since data is displayed using st.bar_chart() directly)

## Usage

```python
import streamlit as st
from fundamentals import StockFundamentalsFactory
from src.sfundamentals import StreamlitIncomeStatements, StreamlitCashFlows, StreamlitBalanceSheets


def main():
    st.title("Application title")
    
    # Initialize factory.
    stock_factory = StockFundamentalsFactory(symbol="aapl", api_key="abc123")

    # Get data using factory.
    income_statements = stock_factory.income_statement(period="quarter", limit=40)
    balance_sheets = stock_factory.balance_sheet(period="quarter", limit=40)
    cash_flows = stock_factory.cash_flow(period="quarter", limit=40)

    # Pass previously computed data as param to streamlit component.
    income_statement_component = StreamlitIncomeStatements(data=income_statements)
    balance_sheet_component = StreamlitBalanceSheets(data=balance_sheets)
    cash_flow_component = StreamlitCashFlows(data=cash_flows)

    # Used to get valid values that can be pass to charting methods.
    inc_stmt_valid_values = income_statement_component.valid_values()
    bal_sheet_valid_values = balance_sheet_component.valid_values()
    cash_flow_valid_values = cash_flow_component.valid_values()

    # print(inc_stmt_valid_values, bal_sheet_valid_values, cash_flow_valid_values)

    # Use charting methods to display data using st.bar_chart().
    income_statement_component.chart_single_value(value=inc_stmt_valid_values[1])
    balance_sheet_component.chart_multiple_values(values=bal_sheet_valid_values[2:5])
    cash_flow_component.chart_single_value(value=cash_flow_valid_values[-1])

if __name__ == "__main__":
    main()

```
