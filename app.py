#!/usr/bin/python
import json
import os
from tensorflow.keras.preprocessing.image import load_img
import numpy as np
from skimage.io import imsave
from tensorflow.keras import backend as K
from tensorflow.keras.models import load_model


# ==============================
# ========= FLASK ==============
# ==============================  
from flask import Flask, render_template, url_for, request
import requests
import json

app = Flask(__name__)



@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        print("eeefgrrf")
        var = request.form["name"]
        return render_template("machines.html", contenu=[var])
    return render_template("machines.html")

@app.route('/test')
def test():
  return 'test'


