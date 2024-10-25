import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("Task3\LifeExpectancy.csv")
print(df.columns)
print(df.info())

# A.Rename some columns if they contain leading and trailing spaces (by removing spaces).

df.columns = df.columns.str.strip()
print(df.columns)
print(df.info())

# B.Which columns in the dataset have missing values and how many?

missed_value=df.isnull().sum()
print(missed_value)

# C. Drop all the columns from the DataFrame containing more than 15% percent of the missing values.

miss_percentage = df.isnull().mean() *100
print(miss_percentage)

dropped_col = miss_percentage[miss_percentage>15].index
print(dropped_col)

df_clean=df.drop(columns=dropped_col)

print(df_clean.info())

#D. Replace the missing values in the remaining columns with the median

num_cols = df_clean.select_dtypes(include=['int64','float64'])
df_clean[num_cols.columns] = num_cols.fillna(num_cols.median())

print(df_clean.isnull().sum())
print(df_clean.info())