from flask import Flask, redirect,url_for, render_template, request
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import datetime
import pickle
from pandas import to_datetime

app = Flask(__name__)

@app.route("/home")
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/kerala" ,methods=["POST", "GET"])
def kerala():
    if request.method == "POST":
        date = list()
        dat=request.form["nm"]
        date.append([dat])
        date = pd.DataFrame(date)
        date.columns = ['ds']
        date['ds'] = to_datetime(date['ds'])
        with open('Kerala.pkl', 'rb') as f:
            model = pickle.load(f)
        forecast = model.predict(date)
        x=forecast.iloc[ : ,3].values
        return redirect(url_for("predict",pred=x))

    else:
        return render_template("state.html")

@app.route("/tn" ,methods=["POST", "GET"])
def tn():
    if request.method == "POST":
        date = list()
        dat=request.form["nm"]
        date.append([dat])
        date = pd.DataFrame(date)
        date.columns = ['ds']
        date['ds'] = to_datetime(date['ds'])
        with open('TamilNadu.pkl', 'rb') as f:
            model = pickle.load(f)
        forecast = model.predict(date)
        x=forecast.iloc[ : ,3].values
        return redirect(url_for("predict",pred=x))

    else:
        return render_template("state.html")

@app.route("/<pred>")
def predict(pred):
    return render_template("predict.html", id=pred)

if __name__ == "__main__":
    app.run(debug=True)
