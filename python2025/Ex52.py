import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="whitegrid")

data = pd.read_csv(r"C:\python2025\WA_Fn-UseC_-HR-Employee-Attrition.csv")
import warnings
warnings.filterwarnings("ignore")

data.head()
data.sample(10)
data.shape
data.describe()
data.info()
data['Age'].describe()

plt.figure(figsize=(10, 6))

ax = sns.histplot(data['Age'], bins=50, kde=True, palette='viridis')

plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.xticks([i for i in range(15, 100, 5)])

plt.show()

sns.jointplot(hr.Age,hr.MonthlyIncome, kind = "scatter")   
plt.show()


data['Attrition'].value_counts()
attrition_rate = data['Attrition'].value_counts(normalize=True) * 100
print(attrition_rate)

attrition= data['Attrition'].value_counts()

plt.figure(figsize=(10, 6))

sns.barplot(x=attrition.index, y=attrition.values, palette='viridis')

plt.title('Attrition')
plt.xlabel('\nJob')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')

plt.show()

import matplotlib.pyplot as plt

# Count the values
Department = data['Department'].value_counts()

# Create pie chart
plt.figure(figsize=(8, 8))
plt.pie(Department.values, labels=Department.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.viridis.colors)

# Add title
plt.title('Department Distribution')

# Show plot
plt.show()

data['EducationField'].value_counts()
EducationField= data['EducationField'].value_counts()


plt.figure(figsize=(10, 6))


sns.barplot(x=EducationField.index, y=EducationField.values, palette='viridis')


plt.title('EducationField')
plt.xlabel('\nfieldd')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')

plt.show()

data['Gender'].value_counts()
import warnings
warnings.filterwarnings("ignore")

Gender= data['Gender'].value_counts()


plt.figure(figsize=(10, 6))


sns.barplot(x=Gender.index, y=Gender.values, palette='viridis')


plt.title('Gender')
plt.xlabel('\nGender')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')


plt.show()

data['MaritalStatus'].value_counts()
marital_counts = data['MaritalStatus'].value_counts()


plt.figure(figsize=(12, 6))


sns.barplot(x=marital_counts.index, y=marital_counts.values, palette='viridis')


plt.title('Count of Each Marital-Status Category')
plt.xlabel('\nMarital-Status')
plt.ylabel('Count')

plt.show()

data['DailyRate'].describe()
plt.figure(figsize=(10, 6))


sns.kdeplot(data['DailyRate'], palette='viridis')



plt.title('DailyRate')
plt.xlabel('rate')
plt.ylabel('y')


plt.show()

data['MonthlyRate'].describe()
plt.figure(figsize=(10, 6))

sns.kdeplot(data['MonthlyRate'], palette='magma')


plt.title('MonthlyRate')
plt.xlabel('rate')
plt.ylabel('y')

plt.show()

data['OverTime'].value_counts()
OverTime= data['OverTime'].value_counts()


plt.figure(figsize=(10, 6))


sns.barplot(x=OverTime.index, y=OverTime.values, palette='magma')


plt.title('OverTime')
plt.xlabel('\nOverTime')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')

plt.show()


data['DistanceFromHome'].value_counts()
DistanceFromHome= data['DistanceFromHome'].value_counts()

plt.figure(figsize=(10, 6))

sns.barplot(x=DistanceFromHome.index, y=DistanceFromHome.values, palette='magma')

plt.title('DistanceFromHome')
plt.xlabel('\nDistanceFromHome')
plt.ylabel('Dis')
plt.xticks(rotation=45, ha='right')

plt.show()

data['MonthlyIncome'].value_counts()
MonthlyIncome= data['MonthlyIncome'].value_counts()

# Define figure size
plt.figure(figsize=(10, 6))

# Plot bar chart
sns.barplot(x=MonthlyIncome.index, y=MonthlyIncome.values, palette='magma')

# Add labels and title
plt.title('MonthlyIncome')
plt.xlabel('\nMonthlyIncome')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')

import seaborn as sns
import matplotlib.pyplot as plt

sns.boxplot(x='Attrition', y='MonthlyIncome', data=data)
plt.title("MonthlyIncome")
plt.show()


sns.boxplot(x='Attrition', y='DistanceFromHome', data=data)
plt.title("effect of Distance from home")
plt.show()


