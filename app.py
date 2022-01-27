# import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import sng
import os
import sys
# import logging

# Create flask app
flask_app = Flask(__name__)
# flask_app.logger.addHandler(logging.StreamHandler(sys.stdout))
# flask_app.logger.setLevel(logging.ERROR)
model = sng.Generator.load('my_model.pkl')

@flask_app.route("/")
def Home():
    return render_template("index.html")

@flask_app.route("/predict", methods = ["POST"])
def predict():
    float_features = request.form.get("num_predictions")
    # print (float_features)
    # features = [np.array(float_features)]
    prediction = model.simulate(n=int(float_features))
    return render_template("index.html", prediction_text = "Generated names of artists/DJs: {}".format(prediction))

if __name__ == "__main__":
    flask_app.run(debug=True)
