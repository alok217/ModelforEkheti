import pandas
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline
import keras
import sys
import json
import requests
import numpy as np
import os

from flask import Flask, request
from model import prediction
app = Flask(__name__)

@app.route("/",methods = ['POST'])
def home():
    # print(request.form)
    data=request.form.get('data')
    print(data)
    h = prediction(str(data))
    # print('hi',h)
    return str(h)
    # return "Hi"
    
if __name__ == "__main__":
    app.run(debug=True)
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
