# -*- coding: utf-8 -*-
"""Pandas_Tutorial.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qCN_-vRb2JsZw9AZhb1fNH_0021nzek9

# Pandas

[Official Project Docs](https://pandas.pydata.org/pandas-docs/stable/reference/index.html)

https://pandas.pydata.org/pandas-docs/stable/reference/index.html
"""

!pip install pandas

import pandas as pd

"""## Dataset from local file"""

housing_df = pd.read_csv('sample_data/california_housing_train.csv')
housing_df.shape

housing_df.head()

housing_df.tail()

housing_df.columns

housing_df[['longitude', 'latitude', 'population']].iloc[10:12]

housing_df['population'] = housing_df['population'].astype(int)
housing_df['population'].head(3)

housing_df.housing_median_age.hist(bins=20)

housing_df.plot.scatter(x='median_house_value', y='median_income')

housing_df.describe()

"""## Datasets in python modules

"""

from sklearn import datasets

iris = datasets.load_iris()
print(type(iris.data))
print(type(iris.feature_names))

iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
iris_df.head(10)

# this is an example of "broacasting"
iris_df['species_code'] = iris.target
iris_df['species_name'] = iris.target_names[iris.target]

iris_df.head(10)

# slicing
#iris_df[5:7]
#iris_df[::10]

#filtering
iris_df[(iris_df['petal length (cm)'] > 6.5)]

iris_df['petal length (cm)'] > 6.5

# can we find the probability that something is a 'virginica' iris given that it has a petal length of > 6.0cm?

#len(iris_df[(iris_df.species_name == 'virginica') & (iris_df['petal length (cm)'] > 6.5)]) / len(iris_df)
prob_virg_and_long_petal = len(iris_df[(iris_df.species_name == 'virginica') & (iris_df['petal length (cm)'] > 6.5)]) / len(iris_df)
prob_long_petal = len(iris_df[(iris_df['petal length (cm)'] > 6.5)]) / len(iris_df)
# P(V | LP) = P(V ^ LP) / P(LP)
prob_virg_and_long_petal / prob_long_petal

iris_df.plot.scatter(x='petal length (cm)', y='sepal width (cm)', c='species_code', colormap='Set1', colorbar=False)

# easier example of broadcasting change cm->mm
iris_df['sepal length (mm)'] = 10 * iris_df['sepal length (cm)']
iris_df.head(3)

# drop old column
iris_df.drop(columns=['sepal length (cm)'], inplace=True)
iris_df.head(3)

"""## Dataset from url"""

corp_df = pd.read_csv('https://drive.google.com/uc?id=13a2WyLoGxQKXbN_AIjrOogIlQKNe9uPm&export=download')
corp_df.head()

corp_df.shape

corp_df.dtypes

# can we figure out the probabilities of a company in this dataset being part of some particular industry?

corp_df.Industry.value_counts()

corp_df.Industry.value_counts() / len(corp_df)

(100.0 * corp_df.Industry.value_counts() / len(corp_df)).rename('percent')

