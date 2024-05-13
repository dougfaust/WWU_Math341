"""
MATH 341 programming assignment 4
Student:
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
# remember to import seaborn, bokeh or plotly here as needed

def download_clean_mnist():
    # sklearn bunch object, similar to a dictionary
    digits = load_digits(as_frame=True)
    print(digits.data.shape)

    # a pandas dataframe with target merged as a column
    df = pd.DataFrame(data=digits.data, columns=digits.feature_names)
    df['label'] = digits.target

    return digits, df

def plot_sample_digits(d):
    print(f"Example format of raw data:\n{d.images[8]}\nLabel: {d.target[8]}")
    _, axes = plt.subplots(nrows=1, ncols=4, figsize=(10, 3))
    for ax, image, label in zip(axes, d.images, d.target):
        ax.set_axis_off()
        ax.imshow(image, cmap=plt.cm.gray_r, interpolation="nearest")
        ax.set_title("Digit Label: %i" % label)

    return None

def problem_one(df):
    # code to add two new features here
    return df

def problem_two(df, feature):
    assert feature in list(df.columns)
    # code to plot boxplots of feature grouped by label
    return

def problem_three():
    return df

def problem_four():
    # print the answer to stdout
    return

def problem_five():
    pass

def problem_six():
    pass

if name == "__main__":

    digits, mnist_df = download_clean_mnist()

    plot_sample_digits(digits)

    # compare to the format of the dataframe:
    print(mnist_df.head())

    df = problem_one(df)
    print(f"my new columns should be in this list: {df.columns}")

    # what does this do?
    # mnist_df[['pixel_5_5', 'label']].boxplot(by='label')
    problem_two(mnist_df, feature)

    iris_df = problem_three()

    problem_four(iris_df)

    problem_five(iris_df)

    problem_six()
