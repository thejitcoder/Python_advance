import pandas as pd

df= pd.read_csv('student1.csv')
print(df)

df_no_duplicates = df.drop_duplicates()

print(df_no_duplicates)
