import pandas as pd

df= pd.read_csv('student1.csv')
print(df)


# NAN : In a csv file nan stands for not a number. It is the part of the data cleaning. Where one column value is missed - It creates a problem in analytics. 
# Solution : That column value make it NAN and then covert that NAN to 0 and 1 , which helps in create graphs. 