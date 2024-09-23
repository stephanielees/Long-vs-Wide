import pandas as pd

# wide format
# data source: https://data.bls.gov/toppicks?survey=bls
cpi = pd.read_excel('usa_inflation_series_bls.xlsx', skiprows=11)
cpi.drop(['HALF1', 'HALF2'], axis=1, inplace=True)
print("---- CPI in The U.S. ----")
print("BEFORE PIVOTING: WIDE FORMAT")
print(f"Total years in this dataset is the total rows, which is: {cpi.shape[0]}")
print("Total months: 12")
print(cpi.head())
input()

cpi_long = pd.melt(cpi, id_vars=['Year'], var_name='Month', value_name='cpi')
cpi_long['Date'] = [pd.to_datetime(f'{mm} {yy}') for mm, yy in zip(cpi_long.Month, cpi_long.Year)]
cpi_long = cpi_long.sort_values(by=['Date'])
cpi_long.drop(['Date'], axis=1, inplace=True)
print("AFTER PIVOTING: (SHOULD BE) LONG FORMAT")
print("Is the total rows in the transformed dataset equals to \n",
      "the total rows in the original dataset times 12?", cpi_long.shape[0]==cpi.shape[0]*12)
print(cpi_long.head(20))
input("Press Enter to move on ")

# wide format (example 2)
# data source: https://archive.ics.uci.edu/dataset/396/sales+transactions+dataset+weekly
sales = pd.read_csv('Sales_Transactions_Dataset_Weekly.csv')
sales = sales.iloc[:, :53]
print("---- Sales Transactions Dataset Weekly (from UCI ML Repo) ----")
print("BEFORE PIVOTING: WIDE FORMAT")
print(f"Total products: {sales.shape[0]}, \n total weeks: 52")
print(sales.head())
input()

sales_long = pd.melt(sales, id_vars=['Product_Code'], var_name='Week', value_name='quantity')
print("AFTER PIVOTING")
print("Is the total rows now equals to \n",
      "the total rows in the original dataset times 52?", sales_long.shape[0]==sales.shape[0]*52)
print(sales_long.head())
print(sales_long.iloc[808:815, :])
input("Press Enter to move on ")

# long format
# original data source: https://www.cftc.gov/MarketReports/CommitmentsofTraders/index.htm
cot = pd.read_excel('myFinComYY.xls', parse_dates=['Report_Date_as_MM_DD_YYYY'])
print("---- Excerpt of COT Report ----")
print("BEFORE PIVOTING: LONG FORMAT")
print(f"The original shape: {cot.shape}")
print(f"Total unique values in Market names: {len(cot.Market_and_Exchange_Names.unique())}")
print(f"Total unique dates: {len(cot.Report_Date_as_MM_DD_YYYY.unique())}")
print(f"Column names: {cot.columns}")
print(cot.head(10))
input()

cot = cot.pivot(columns='Market_and_Exchange_Names', index='Report_Date_as_MM_DD_YYYY')
print("AFTER PIVOTING")
print(f"Is the total columns now equals to \n",
      f"the total Market times two? {(cot.shape[1]) == int(67 * 2)}") #shape excludes index

print(f"The dataframe shape after pivoting: {cot.shape}")
print(cot.head())
input("Press Enter to move on")

# long format 2
# data source: https://www.kaggle.com/competitions/tabular-playground-series-jan-2022/data
merch = pd.read_csv('kaggle_train.csv', parse_dates=['date'])
merch = merch.iloc[:, 1:]
print("---- Kaggle Tabular Playground Series Jan 2022 ----")
print("BEFORE PIVOTTING: LONG FORMAT")
print(f"The original shape: {merch.shape}")
print(merch.head())
print(f"Unique countries: {merch.country.unique()} \n"
      f"Unique stores: {merch.store.unique()} \n"
      f"Unique products: {merch['product'].unique()} \n"
      f"Date range (unique dates): {merch.date.max() - merch.date.min()} \n"
      f"from {merch.date.min()} to {merch.date.max()}")

merch_wide = merch.pivot(columns=['country', 'store'], index=['product', 'date'])
print("AFTER PIVOTTING")
print(merch_wide.head())