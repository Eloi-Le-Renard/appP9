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
        #url = "https://functionp9.azurewebsites.net/api/httptrigger2"
        url = "https://nom-aplip9.azurewebsites.net/api/HttpTrigger2?code=Bon37HsVudCSsACK7XjHCHNEp2oUQ2Gg_Awi5hH3rr5TAzFuGkmn8w=="
        url = "https://p9appf.azurewebsites.net/api/HttpTrigger1?"
        params = {'userID': str(user_id)}
        x = requests.post(url, params=params)
        #x = requests.get(url+"?name=12")
        ##x = requests.get(url)
        ##jsonString = json.dumps(x.json())
        var = x.text
        
        # methode post input id client
        #var = request.form["name"]
        
        return render_template("machines.html", contenu=[var])
    return render_template("machines.html")

@app.route('/test')
def test():
  return 'test'


