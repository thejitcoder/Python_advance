import pandas as pd
import matplotlib.pyplot as plt

#Load data from CSV file
data = pd.read_csv('car.csv')

#Plot pie chart
plt.figure(figsize=(8, 8))
plt.pie(data['Sales'], labels=data['Car name'], autopct='%1.1f%%')
plt.title('Car Sales Distribution')
plt.show()
