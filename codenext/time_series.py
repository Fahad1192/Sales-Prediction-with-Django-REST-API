#!/usr/bin/env python
# coding: utf-8


def timeseries_pred(input):
    
    import numpy as np
    import pandas as pd
    from sklearn.ensemble import RandomForestRegressor
    
    # Importing the dataset
    dataset = pd.read_csv('SalesData.csv')
    X = dataset.iloc[:, 1:2].values
    y = dataset.iloc[:, 6:7].values
    
    
    regressor = RandomForestRegressor()
    regressor.fit(X, y.ravel())
    output = regressor.predict(np.array([[input]]))
    return output

print(timeseries_pred(80))