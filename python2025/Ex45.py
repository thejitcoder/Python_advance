import numpy as np  # Linear algebra
import pandas as pd  # Data processing, CSV file I/O
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.rdfead_csv('c:/python2025/mall_customers.csv')

# Data inspection
print(df.describe())
print(df.isnull().sum())
print(df.shape)
print(df.info())
print(type(df))

# Visualization
sns.countplot(x="Gender", data=df)
plt.title("Count of Gender")
plt.show()

sns.histplot(df["Age"], kde=True)
plt.title("Age Distribution")
plt.show()

sns.histplot(df["Annual Income (k$)"], kde=True)
plt.title("Annual Income Distribution")
plt.show()

sns.histplot(df["Spending Score (1-100)"], kde=True)
plt.title("Spending Score Distribution")
plt.show()

# Pairplot (Convert 'Gender' to numeric for compatibility, if needed)
df_encoded = df.copy()
df_encoded["Gender"] = df_encoded["Gender"].astype("category").cat.codes
sns.pairplot(df_encoded[["Gender", "Age", "Annual Income (k$)", "Spending Score (1-100)"]])
plt.show()

# Pie chart for Gender
Gender_counts = df['Gender'].value_counts()
plt.pie(Gender_counts, labels=Gender_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Gender Distribution')
plt.axis('equal')
plt.show()

# Clustering with KMeans
from sklearn.cluster import KMeans

# Data for clustering
data = df.iloc[:, [2, 4]].values  # Age and Spending Score

# Elbow Method
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=0)
    kmeans.fit(data)
    wcss.append(kmeans.inertia_)

plt.plot(range(1, 11), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()

#Plotting the clusters

import matplotlib.pyplot as plt
y_kmeans = kmeans.fit_predict(data)
fig, ax = plt.subplots(figsize=(14, 6))

# Plot each cluster
ax.scatter(data[y_kmeans == 0, 0], data[y_kmeans == 0, 1], s=100, c='red', label='Cluster 1')
ax.scatter(data[y_kmeans == 1, 0], data[y_kmeans == 1, 1], s=100, c='blue', label='Cluster 2')
ax.scatter(data[y_kmeans == 2, 0], data[y_kmeans == 2, 1], s=100, c='green', label='Cluster 3')
ax.scatter(data[y_kmeans == 3, 0], data[y_kmeans == 3, 1], s=100, c='cyan', label='Cluster 4')

# Plot the centroids
ax.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], 
           s=400, c='yellow', label='Centroid')

# Chart formatting
plt.title('Cluster Segmentation of Customers')
plt.xlabel('Age')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()
