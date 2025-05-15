import numpy as np # linear algebra
import pandas as pd # data processing
import plotly.express as px

import matplotlib as plt
import apyori
from apyori import apriori
data = pd.read_csv("../PYTHON2025/Groceries_dataset.csv")
data.shape
data.info()
data.isna().sum()
x = data['itemDescription'].value_counts().sort_values(ascending=False)[:10]
print("Top 10 frequently sold products")
fig = px.bar(x= x.index, y= x.values)
fig.update_layout(title_text= "Top 10 frequently sold products ", xaxis_title= "Products", yaxis_title="Number of item sold")
fig.show()

import matplotlib.pyplot as plt

# Example data
x = [1, 2, 3, 4, 5]
y = [10, 15, 13, 17, 20]

# Create scatter plot
plt.scatter(x, y)

# Add labels and title
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Scatter Plot Example')

# Show the plot
plt.show()

# importing libraries 
import matplotlib.pyplot as plt 
import seaborn 

# declaring data 
data = [44, 45, 40, 41, 39] 
keys = ['Class 1', 'Class 2', 'CLass 3', 'Class 4', 'Class 5'] 

# define Seaborn color palette to use 
palette_color = seaborn.color_palette('bright') 

# plotting data on chart 
plt.pie(data, labels=keys, colors=palette_color, autopct='%.0f%%') 

# displaying chart 
plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = {
    'Product': ['Bread', 'Milk', 'Butter', 'Eggs', 'Cheese', 'Jam', 'Yogurt', 'Juice', 'Soda', 'Cereal'],
    'Number of item sold': [120, 95, 75, 130, 85, 60, 70, 100, 110, 90]
}

df = pd.DataFrame(data)

# Histogram plot
sns.histplot(df["Number of item sold"], kde=True, bins=5, color='skyblue')
plt.title("Distribution of Number of Items Sold")
plt.xlabel("Number of Items Sold")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()




