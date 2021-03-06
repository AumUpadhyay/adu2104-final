# -*- coding: utf-8 -*-
"""
Created on Fri May 8 23:00:17 2020

@author: Aum Upadhyay
"""

#import statements
from flask import Flask, render_template, url_for

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def hello():
    return render_template("index.html")

#static route
@app.route("/assignments")
def assignments():
    return render_template("assignments.html")

#static route
@app.route("/classes")
def classes():
    return render_template("classes.html")

#start the server
if __name__ == "__main__":
    app.run()