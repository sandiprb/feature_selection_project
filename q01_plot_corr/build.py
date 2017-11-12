import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.read_csv('data/house_prices_multivariate.csv')


# Write your solution here:
def plot_corr(data,size=11):
    sns.heatmap(data.corr())
    plt.show()
