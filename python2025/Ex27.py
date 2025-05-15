#Draw this as a bargraph

import pandas as pd
import matplotlib.pyplot as plt

#Load the CSV file
df = pd.read_csv('car.csv')

#Plot the bar graph
plt.figure(figsize=(10,6))
plt.bar(df['Car name'], df['Sales'])
plt.xlabel('Car name')
plt.ylabel('Sales')
plt.title('Car Sales')
plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to fit labels
plt.show()

