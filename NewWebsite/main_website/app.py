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
        with open('models/Kerala.pkl', 'rb') as f:
            model = pickle.load(f)
        forecast = model.predict(date)
        x=forecast.iloc[ : ,3].values
        return redirect(url_for("predict",pred=x))

    else:
        return render_template("state.html")

@app.route("/tamilnadu" ,methods=["POST", "GET"])
def tn():
    if request.method == "POST":
        date = list()
        dat=request.form["nm"]
        date.append([dat])
        date = pd.DataFrame(date)
        date.columns = ['ds']
        date['ds'] = to_datetime(date['ds'])
        with open('models/TamilNadu.pkl', 'rb') as f:
            model = pickle.load(f)
        forecast = model.predict(date)
        x=forecast.iloc[ : ,3].values
        return redirect(url_for("predict",pred=x))

    else:
        return render_template("state.html")

@app.route("/karnataka" ,methods=["POST", "GET"])
def kn():
    if request.method == "POST":
        date = list()
        dat=request.form["nm"]
        date.append([dat])
        date = pd.DataFrame(date)
        date.columns = ['ds']
        date['ds'] = to_datetime(date['ds'])
        with open('models/Karnataka.pkl', 'rb') as f:
            model = pickle.load(f)
        forecast = model.predict(date)
        x=forecast.iloc[ : ,3].values
        return redirect(url_for("predict",pred=x))

    else:
        return render_template("state.html")

@app.route("/westbengal" ,methods=["POST", "GET"])
def wb():
    if request.method == "POST":
        date = list()
        dat=request.form["nm"]
        date.append([dat])
        date = pd.DataFrame(date)
        date.columns = ['ds']
        date['ds'] = to_datetime(date['ds'])
        with open('models/WestBengal.pkl', 'rb') as f:
            model = pickle.load(f)
        forecast = model.predict(date)
        x=forecast.iloc[ : ,3].values
        return redirect(url_for("predict",pred=x))

    else:
        return render_template("state.html")

@app.route("/telangana" ,methods=["POST", "GET"])
def telangana():
    if request.method == "POST":
        date = list()
        dat=request.form["nm"]
        date.append([dat])
        date = pd.DataFrame(date)
        date.columns = ['ds']
        date['ds'] = to_datetime(date['ds'])
        with open('models/Telangana.pkl', 'rb') as f:
            model = pickle.load(f)
        forecast = model.predict(date)
        x=forecast.iloc[ : ,3].values
        return redirect(url_for("predict",pred=x))

    else:
        return render_template("state.html")

@app.route("/rajasthan" ,methods=["POST", "GET"])
def rajasth():
    if request.method == "POST":
        date = list()
        dat=request.form["nm"]
        date.append([dat])
        date = pd.DataFrame(date)
        date.columns = ['ds']
        date['ds'] = to_datetime(date['ds'])
        with open('models/Rajasthan.pkl', 'rb') as f:
            model = pickle.load(f)
        forecast = model.predict(date)
        x=forecast.iloc[ : ,3].values
        return redirect(url_for("predict",pred=x))

    else:
        return render_template("state.html")

@app.route("/maharashtra" ,methods=["POST", "GET"])
def mh():
    if request.method == "POST":
        date = list()
        dat=request.form["nm"]
        date.append([dat])
        date = pd.DataFrame(date)
        date.columns = ['ds']
        date['ds'] = to_datetime(date['ds'])
        with open('models/maharashtra.pkl', 'rb') as f:
            model = pickle.load(f)
        forecast = model.predict(date)
        x=forecast.iloc[ : ,3].values
        return redirect(url_for("predict",pred=x))

    else:
        return render_template("state.html")

@app.route("/gujarat" ,methods=["POST", "GET"])
def gujarat():
    if request.method == "POST":
        date = list()
        dat=request.form["nm"]
        date.append([dat])
        date = pd.DataFrame(date)
        date.columns = ['ds']
        date['ds'] = to_datetime(date['ds'])
        with open('models/Gujarat.pkl', 'rb') as f:
            model = pickle.load(f)
        forecast = model.predict(date)
        x=forecast.iloc[ : ,3].values
        return redirect(url_for("predict",pred=x))

    else:
        return render_template("state.html")

@app.route("/delhi" ,methods=["POST", "GET"])
def delhi():
    if request.method == "POST":
        date = list()
        dat=request.form["nm"]
        date.append([dat])
        date = pd.DataFrame(date)
        date.columns = ['ds']
        date['ds'] = to_datetime(date['ds'])
        with open('models/Delhi.pkl', 'rb') as f:
            model = pickle.load(f)
        forecast = model.predict(date)
        x=forecast.iloc[ : ,3].values
        return redirect(url_for("predict",pred=x))

    else:
        return render_template("state.html")

@app.route("/bihar" ,methods=["POST", "GET"])
def bihar():
    if request.method == "POST":
        date = list()
        dat=request.form["nm"]
        date.append([dat])
        date = pd.DataFrame(date)
        date.columns = ['ds']
        date['ds'] = to_datetime(date['ds'])
        with open('models/Bihar.pkl', 'rb') as f:
            model = pickle.load(f)
        forecast = model.predict(date)
        x=forecast.iloc[ : ,3].values
        return redirect(url_for("predict",pred=x))

    else:
        return render_template("state.html")

@app.route("/andhrapradesh" ,methods=["POST", "GET"])
def ap():
    if request.method == "POST":
        date = list()
        dat=request.form["nm"]
        date.append([dat])
        date = pd.DataFrame(date)
        date.columns = ['ds']
        date['ds'] = to_datetime(date['ds'])
        with open('models/AndhraPradesh.pkl', 'rb') as f:
            model = pickle.load(f)
        forecast = model.predict(date)
        x=forecast.iloc[ : ,3].values
        return redirect(url_for("predict",pred=x))

    else:
        return render_template("state.html")

@app.route("/goa" ,methods=["POST", "GET"])
def goa():
    if request.method == "POST":
        date = list()
        dat=request.form["nm"]
        date.append([dat])
        date = pd.DataFrame(date)
        date.columns = ['ds']
        date['ds'] = to_datetime(date['ds'])
        with open('models/Goa.pkl', 'rb') as f:
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
