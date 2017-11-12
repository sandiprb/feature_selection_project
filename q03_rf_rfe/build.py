# Default imports
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')

from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestClassifier


# Your solution code here

def rf_rfe(df):
    X = df[df.columns[:-1]]
    y = df['SalePrice']
    forest = RandomForestClassifier()
    rfe = RFE(forest, X.columns.size / 2)
    rfe.fit(X, y)
    return list(X.columns[rfe.support_])
