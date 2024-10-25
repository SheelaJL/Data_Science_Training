import pandas as pd
import matplotlib.pyplot as plt


df=pd.read_csv('Task2\Developers.csv')

print (df.head(10))

#check null values
print(df.info())

# Create customized line plots to compare the salary variations Age-wise for Python developer with Javascript developer.

df_needed = df[['Age', 'Python', 'JavaScript']]
print(df_needed)


# Plot JavaScript developer salary age-wise
plt.plot(df_needed['Age'], df_needed['JavaScript'],label="Javascript dev sal", color='m')
plt.xlabel("Age")
plt.ylabel("Javascript")
plt.title("Agewise salary of Javascript developers")



plt.plot(df_needed['Age'], df_needed['Python'],label="Python Dev sal", color='green')
plt.title('Python developer')
plt.ylabel('Python')
plt.xlabel('Age')
plt.legend()
plt.show()

#B.What can you conclude from the comparison?

# Ans:Python developers are receiving good salary when campared to java script developers at all ages.


