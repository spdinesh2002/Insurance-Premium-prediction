import numpy as np
from flask import Flask, request, render_template
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def Home():
    return render_template("home.html")

@app.route("/predict", methods = ["POST"])
def predict():
    features = [x for x in request.form.values()]
    ip = []
    ip.append(int(features[0]))
    ip.append(float(features[2]))
    ip.append(int(features[3]))
    if features[1] == "male":
        ip.extend([0,1])
    elif features[1] == "female":
        ip.extend([1,0])
    if features[4] == "no":
        ip.extend([1,0])
    elif features[4] == "yes":
        ip.extend([0,1])
    if features[5] == "northeast":
        ip.extend([1,0,0,0])
    elif features[5] == "northwest":
        ip.extend([0,1,0,0])
    elif features[5] == "southeast":
        ip.extend([0,0,1,0])
    elif features[5] == "southwest":
        ip.extend([0,0,0,1])
    ipf = []
    ipf.append(ip)
    prediction = model.predict(ipf)
    return render_template("home.html", ans = "Your predicted insurance expense: {}".format(prediction[0]))

if __name__ == "__main__":
    app.run(debug=True)