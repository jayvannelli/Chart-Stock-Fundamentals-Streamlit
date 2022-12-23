
VALID_INCOME_STATEMENT_VALUES: list[str] = [
    "revenue", "costOfRevenue", "grossProfit", "grossProfitRatio", "researchAndDevelopmentExpenses",
    "generalAndAdministrativeExpenses", "sellingAndMarketingExpenses", "sellingGeneralAndAdministrativeExpenses",
    "otherExpenses", "operatingExpenses", "costAndExpenses", "interestIncome", "interestExpense",
    "depreciationAndAmortization", "ebitda", "ebitdarati", "operatingIncome", "operatingIncomeRatio",
    "totalOtherIncomeExpensesNet", "incomeBeforeTax", "incomeBeforeTaxRatio", "incomeTaxExpense",
    "netIncome", "netIncomeRatio", "eps", "epsdiluted", "weightedAverageShsOut", "weightedAverageShsOutDil",
]

VALID_CASH_FLOW_VALUES: list[str] = [
    "netIncome", "depreciationAndAmortization", "deferredIncomeTax", "stockBasedCompensation",
    "changeInWorkingCapital", "accountsReceivables", "inventory", "accountsPayables", "otherWorkingCapital",
    "otherNonCashItems", "netCashProvidedByOperatingActivities", "investmentsInPropertyPlantAndEquipment",
    "acquisitionsNet", "purchasesOfInvestments", "salesMaturitiesOfInvestments", "otherInvestingActivites",
    "netCashUsedForInvestingActivites", "debtRepayment", "commonStockIssued", "commonStockRepurchased",
    "dividendsPaid", "otherFinancingActivites", "netCashUsedProvidedByFinancingActivities", "effectOfForexChangesOnCash",
    "netChangeInCash", "cashAtEndOfPeriod", "cashAtBeginningOfPeriod", "operatingCashFlow", "capitalExpenditure",
    "freeCashFlow",
]

VALID_BALANCE_SHEET_VALUES: list[str] = [
    "cashAndCashEquivalents", "shortTermInvestments", "cashAndShortTermInvestments", "netReceivables",
    "inventory", "otherCurrentAssets", "totalCurrentAssets", "propertyPlantEquipmentNet", "goodwill",
    "intangibleAssets", "goodwillAndIntangibleAssets", "longTermInvestments", "taxAssets",
    "otherNonCurrentAssets", "totalNonCurrentAssets", "otherAssets", "totalAssets", "accountPayables",
    "shortTermDebt", "taxPayables", "deferredRevenue", "otherCurrentLiabilities", "totalCurrentLiabilities",
    "longTermDebt", "deferredRevenueNonCurrent", "deferredTaxLiabilitiesNonCurrent", "otherNonCurrentLiabilities",
    "totalNonCurrentLiabilities", "otherLiabilities", "capitalLeaseObligations", "totalLiabilities",
    "preferredStock", "commonStock", "retainedEarnings", "accumulatedOtherComprehensiveIncomeLoss",
    "othertotalStockholdersEquity", "totalStockholdersEquity", "totalLiabilitiesAndStockholdersEquity",
    "minorityInterest", "totalEquity", "totalLiabilitiesAndTotalEquity", "totalInvestments", "totalDebt", "netDebt"
]
