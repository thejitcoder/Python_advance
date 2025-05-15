import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('c:/python2025/mall_customers.csv')
print(1)
print(df.head(10))

print(df.describe())
print(df.isnull().sum())
print(df.shape)

print(df.info())
print(type(df))

sns.countplot(df['Gender'])
df['Gender'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('Gender Distribution')
plt.ylabel('')  # Optional: removes y-axis label
plt.show()
sns.histplot(df['Age'], kde=True)
plt.show()


sns.distplot(df['Annual Income (k$)'])
plt.show()

sns.distplot(df['Spending Score (1-100)'])
plt.show()

sns.pairplot(df[['Gender' , 'Age' , 'Annual Income (k$)' , 'Spending Score (1-100)']])
plt.show()

data = df.iloc[:, [2,4]].values
from sklearn.cluster import KMeans
wcss=[] # within cluster sum of square
for i in range (1,11):kmeans= KMeans (n_clusters=i, init='k-means+ I+', random_state=0)
kmeans.fit(data)
wcss.append(kmeans.inertia_) # inertia_ = to find the wcss value

plt.plot(range (1,11), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')




