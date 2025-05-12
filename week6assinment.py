# TASK ONE 
# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load Iris dataset
try:
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
except Exception as e:
    print("Error loading the dataset:", e)

# Display first few rows
df.head()

# Check data types and missing values
df.info()
df.isnull().sum()


# Clean dataset (no missing values, so this is just in case)
df.dropna(inplace=True)


#TASK TWO 

# Basic statistics
df.describe()
# Grouping by species and getting mean
grouped = df.groupby('species').mean()
grouped

# Interesting observations
for column in df.columns[:-1]:  # skip 'species'
    print(f"\nMean {column} by species:")
    print(df.groupby('species')[column].mean())

#TASK THREE
grouped.T.plot(kind='line', marker='o')
plt.title('Average Feature Measurements by Species')
plt.ylabel('Measurement (cm)')
plt.xlabel('Features')
plt.legend(title='Species')
plt.grid(True)
plt.tight_layout()
plt.show()


sns.barplot(x='species', y='petal length (cm)', data=df)
plt.title('Average Petal Length by Species')
plt.ylabel('Petal Length (cm)')
plt.xlabel('Species')
plt.show()


plt.hist(df['sepal length (cm)'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribution of Sepal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()


sns.scatterplot(data=df, x='sepal length (cm)', y='petal length (cm)', hue='species')
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Species')
plt.grid(True)
plt.show()


