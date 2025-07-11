"""
MATH 341 programming assignment 5
Student:
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from scipy import stats

def download_clean_mnist():
    # sklearn bunch object, similar to a dictionary
    digits = load_digits(as_frame=True)

    # a pandas dataframe with informative features and target merged as a column
    df = pd.DataFrame(data=digits.data, columns=digits.feature_names)
    center_pixels = ['pixel_3_3', 'pixel_3_4', 'pixel_4_3', 'pixel_4_4']
    df['CENTER_SUM'] = df[center_pixels].sum(axis=1)

    df['label'] = digits.target

    return df

def clt_samples(dist, n=5, samples=1000):
    """this finds the mean of n random values from your dist, samples times"""
    s = []
    for _ in range(samples):
        s.append(dist.rvs(size=n).mean())
    return s

def clt_visualizer():
    
    # get an example model from the scipy stats package: the Weibull distribution takes a parmater c
    c = 2
    rv = stats.weibull_min(c)

    # choose the sample space (you might need to fiddle with this to see all your data)
    # for a discrete distribution, x will need to be an array of integers
    x = np.linspace(0.01, 2.99, 300)

    fig, (ax1, ax2) = plt.subplots(2, sharex=True)
    ax1.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')
    ax2.hist(clt_samples(rv), bins=75, range=[0, 2.5], alpha=0.3, label='mean:   5 samples')
    ax2.hist(clt_samples(rv, 25), bins=75, range=[0, 2.5], alpha=0.3, label='mean:  25 samples')
    ax2.hist(clt_samples(rv, 100), bins=75, range=[0, 2.5], alpha=0.3, label='mean: 100 samples')

    ax1.set_ylabel('PDF')
    ax2.set_ylabel('Histogram of 1000 sample means')

    fig.suptitle('Weibull distribution: Underlying PDF and sample mean distributions')
    plt.legend(loc='upper right')
    plt.show()

def problem_one_continuous():
    """copy and modify the clt_visualizer method code for a different continuous distribution"""
    return

def problem_one_discrete():
    """copy and modify the clt_visualizer method code for a discrete distribution 
    remember x must be an array of integers"""
    return

def problem_two(df, label):
    # here's a good start, this gets you an array of the CENTER_SUM value for a particular label:
    feature_values = df[df.label == label].CENTER_SUM.values
    return

def problem_three(df, team, alpha):
    # here's a good start, this gets you an array (list) of the goals for D on that team:
    goals_array = df[(df.Team == team) & (df.Pos == 'D')]['G'].values
    return

def problem_four(df, team):
    return

def problem_five(df):

    for k in range(10):
        for j in range(k + 1, 10):
            print(f"ttest for MNIST digits: {k} and {j}")
            print("something about a stats relative ttest?")


if __name__ == "__main__":

    clt_visualizer()

    problem_one_continuous()

    problem_one_discrete()

    mnist_df = download_clean_mnist()
    mnist_df[['CENTER_SUM', 'label']].boxplot(by='label')

    NHL_df = pd.read_csv('https://raw.githubusercontent.com/dougfaust/WWU_Math341/main/data/2023_nhl_stats.csv')

    problem_two(mnist_df, label=9)

    problem_three(NHL_df, 'TOR', 0.95)

    #### Sample vs. population ttest syntax.  How would I find the actual population mean?
    #### use this to solve problem four
    print(stats.ttest_1samp(
        NHL_df[(NHL_df.Team == 'BOS') & (NHL_df.Pos == 'D')]['G'],
        popmean=3.5
    ))

    problem_four(NHL_df, 'WAS')

    """
    this code demonstrates the relative population ttest syntax.
    use this to solve problem five by inserting it into the nested loops
    """
    print(stats.ttest_ind(
                mnist_df[mnist_df.label==1].CENTER_SUM,
                mnist_df[mnist_df.label==9].CENTER_SUM,
                equal_var=False
    ))

    problem_five(mnist_df)
