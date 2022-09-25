#!/usr/bin/python
import os
import numpy as np



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
        user_id = request.form['user_id']
        # call azure f.
        url = "https://p9appf.azurewebsites.net/api/HttpTrigger1?"
        params = {'userID': str(user_id)}
        x = requests.post(url, params=params)
        var = x.text
        
        return render_template("machines.html", contenu=[var])
    return render_template("machines.html")

@app.route('/test')
def test():
  return 'test'


