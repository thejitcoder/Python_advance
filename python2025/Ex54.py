import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="whitegrid")

import warnings
warnings.filterwarnings("ignore")

# Load the dataset
data = pd.read_csv(r"C:\python2025\hranalytics.csv")  # Use raw string for Windows path

# Display basic information
print(data.head())
print(data.sample(10))
print(data.shape)
print(data.describe())
print(data.info())

# Plot distributions
fig, ax = plt.subplots(2, 2, figsize=(12, 10))
plt.suptitle("Understanding the Distribution of Various Factors", fontsize=20)

sns.histplot(data['Age'], kde=True, ax=ax[0, 0])
ax[0][0].set_title('Distribution of Age')

sns.histplot(data['TotalWorkingYears'], kde=True, ax=ax[0, 1])
ax[0][1].set_title('Distribution of Total Working Years')

sns.histplot(data['YearsAtCompany'], kde=True, ax=ax[1, 0])
ax[1][0].set_title('Distribution of Years at Company')

sns.histplot(data['YearsInCurrentRole'], kde=True, ax=ax[1, 1])
ax[1][1].set_title('Distribution of Years in Current Role')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])  # Adjust layout to fit the suptitle
plt.show()


sns.countplot(x=data['Attrition'])
plt.title("Employee Attrition Count")
plt.show()

from numpy import median
sns.barplot(x='Attrition', y='MonthlyIncome', hue='Gender', data=data, estimator=median)
plt.title("Median Monthly Income by Gender and Attrition")
plt.show()

from numpy import median
sns.barplot(x='Attrition', y='MonthlyIncome', hue='JobSatisfaction', data=data, estimator=median)
plt.title("Median Monthly Income by Attrition and Job Satisfaction")
plt.show()


from numpy import median
sns.barplot(x='Attrition', y='MonthlyIncome', hue='MaritalStatus', data=data, estimator=median)
plt.title("Median Monthly Income by Attrition and Marital Status")
plt.show()


f, ax = plt.subplots(figsize=(15, 10))
sns.boxplot(x='JobSatisfaction', y='MonthlyIncome', data=data, hue='JobLevel', palette='Set3')
plt.title("Monthly Income by Job Satisfaction and Job Level")
plt.legend(loc='best')
plt.show()


sns.violinplot(x="Attrition", y="YearsAtCompany", hue="Gender", data=data, palette="muted", split=True, inner="stick")
plt.title("Years at Company by Attrition and Gender")
plt.show()


sns.jointplot(x=data['Age'], y=data['MonthlyIncome'], kind="scatter")
plt.suptitle("Scatter Plot: Age vs Monthly Income", y=1.02)
plt.show()


g = sns.FacetGrid(data, col="JobSatisfaction", row="Gender")
g.map(sns.kdeplot, "MonthlyIncome", "YearsInCurrentRole", fill=True, thresh=0.05)
plt.subplots_adjust(top=0.9)
g.fig.suptitle("KDE Plot of Monthly Income vs. Years in Current Role by Job Satisfaction and Gender")
plt.show()


data1 = ['Attrition', 'Age', 'MonthlyIncome', 'DistanceFromHome']
sns.pairplot(data[data1], kind="reg", diag_kind="kde", hue='Attrition')
plt.suptitle("Pairplot of Selected Features Colored by Attrition", y=1.02)
plt.show()


data2 = ['Gender', 'HourlyRate', 'DailyRate', 'MonthlyRate', 'PercentSalaryHike']
sns.pairplot(data[data2], kind="reg", diag_kind="kde", hue='Gender')
plt.suptitle("Pairplot of Selected Features Colored by Gender", y=1.02)
plt.show()


# Select only numeric columns from the dataset
numeric_data = data.select_dtypes(include=[np.number])

# Plot the correlation heatmap for numeric columns
f, ax = plt.subplots(figsize=(18, 18))
sns.heatmap(numeric_data.corr(), annot=True, linewidths=.4, fmt='.1f', ax=ax)
plt.title("Correlation Heatmap of Numeric Variables")
plt.show()
