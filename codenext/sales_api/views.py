#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from sklearn.externals import joblib
#from sklearn.preprocessing import impute 
#import joblib 
#import pickle


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
# Create your views here.

#reloadModel = joblib.load('./models/RFModelforSales.pickle')

def index(request):
    temp={}
    temp['Week']=77
    #temp['StoreID']=10018
    context={'temp':temp}
    return render(request,'index.html',context)


def predictSales(request):
    if request.method == 'POST':
        temp={}
        temp['Week'] = request.POST.get('WeekVal')
        #temp['StoreID'] = request.POST.get('StoreIDVal')
          

        #print(result)

        #temp2=temp.copy()
        #temp2['Week']=temp['WeekVal']
        #print (temp.keys(),temp2.keys())

        result  = timeseries_pred(temp['Week'])


        testDtaa=pd.DataFrame({'x':temp}).transpose()
        scoreval=result
        context={'scoreval':scoreval,'temp':temp}
        return render(request, 'index.html', context)

