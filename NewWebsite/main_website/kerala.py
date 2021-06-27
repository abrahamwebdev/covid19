import pickle
# pkl_path = "D:\covid19\NewWebsite\main_website\Kerala.pkl"
with open('Kerala.pkl', 'rb') as keralapickle:
    model = pickle.load(keralapickle)