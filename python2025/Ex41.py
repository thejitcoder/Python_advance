import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Load the dataset
data = pd.read_csv("train.csv")
print(data)
print(data.head())

# Correcting the typo in the datetime conversion
data['Order Date'] = pd.to_datetime(data['Order Date'], format='%d/%m/%Y')

# Group sales by date
sales_by_date = data.groupby('Order Date')['Sales'].sum().reset_index()

# Plotting the sales trend
plt.figure(figsize=(12, 6))
plt.plot(sales_by_date['Order Date'], sales_by_date['Sales'], 
         label='Sales', color='red')
plt.title('Sales Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.grid(True)
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()