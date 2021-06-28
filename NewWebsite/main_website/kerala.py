# import pickle
# import datetime
# import pandas as pd

# # pkl_path = "D:\covid19\NewWebsite\main_website\Kerala.pkl"
# date = list()
# dat = '2021-6-11'
# date.append([dat])
# date = pd.DataFrame(date)
# date.columns = ['ds']
# date['ds'] = to_datetime(date['ds'])
# with open('Kerala.pkl', 'rb') as keralapickle:
#     model = pickle.load(keralapickle)
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# from fbprophet import Prophet
import datetime
from pandas import to_datetime
date = list()
dat = '2021-6-28'
date.append([dat])
date = pd.DataFrame(date)
date.columns = ['ds']
date['ds'] = to_datetime(date['ds'])
import pickle
# pkl_path = "Kara.pkl"
# read the Prophet model object
with open('Kerala.pkl', 'rb') as f:
    model = pickle.load(f)
forecast = model.predict(date)
# print(forecast[['ds','yhat','yhat_lower','yhat_upper']])
# k=forecast[['yhat_upper']]
# x=forecast.iloc['yhat_upper'].values
x=forecast.iloc[ : ,3].values
print(x)
# print(forecast)