import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('vd.csv')

print (df.head(10))

#The Year and Publisher columns contain a few missing values. Treat them accordingly.

print(df.info())

# removing null value

df.drop(df[df.Year.isnull()].index, inplace = True) # year
df.drop(df[df.Publisher.isnull()].index, inplace = True) #Publisher

# print missing values
df.info()


# Convert the values contained in the Year column into integer values.

df['Year'] = df['Year'].astype(int)

df.info()

# Find the top 10 most-sold genres of video games sold globally. 

genre = df.groupby('Genre')['Global_Sales'].sum()

top_10 = genre.sort_values(ascending=False).head(10)

print(top_10)


# Create genre-wise bar plots for the total number of units sold across different regions and the world.

genre1_df = df.groupby('Genre')[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']].sum()


sales_df = df.groupby('Genre', as_index = False).sum()

x_axis = sales_df['Genre']
y_axis = sales_df['Global_Sales']

na = genre1_df['NA_Sales']
eu = genre1_df['EU_Sales']
jp = genre1_df['JP_Sales']
os = genre1_df['Other_Sales']
total = genre1_df['Global_Sales']

plt.title('Genre-wise Total Units Sold in Different Regions and Globally')

plt.xlabel('Genre')
plt.ylabel('Total Units Sold')
plt.bar(x_axis, total, label = 'Global')
plt.bar(x_axis, na, label = 'US')
plt.bar(x_axis, eu, label = 'EU')
plt.bar(x_axis, jp, label = 'JP')
plt.bar(x_axis, jp, label = 'OS')
plt.xticks(rotation=90)
plt.legend(bbox_to_anchor =(1, 1))
plt.show()


# What genre of video game is most popular in Japan in terms of the total number of units sold? Also, provide the total number of units sold in Japan for that genre.

most_sales = df.groupby('Genre')['JP_Sales'].sum()


most_sales_japan = most_sales.sort_values(ascending = False).head(1)

print(most_sales_japan)
