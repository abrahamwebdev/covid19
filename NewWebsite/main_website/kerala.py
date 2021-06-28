import pickle
import datetime
import pandas as pd

# pkl_path = "D:\covid19\NewWebsite\main_website\Kerala.pkl"
date = list()
dat = '2021-6-11'
date.append([dat])
date = pd.DataFrame(date)
date.columns = ['ds']
date['ds'] = to_datetime(date['ds'])
with open('Kerala.pkl', 'rb') as keralapickle:
    model = pickle.load(keralapickle)
