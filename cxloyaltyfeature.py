from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd
import numpy as np
class cxloyaltyfeature(BaseEstimator, TransformerMixin):
  def __init__(self):
    pass

  def fit(self, X, y=None):
    return self

  def transform(self, X):
    data = X.copy()
    data['recency'] = data['recency'].replace(0,1)
    data['cx_loyalty'] = data['customer_since']/data['recency']
    data = data.drop(columns = ['customer_since', 'recency'])
    return data
