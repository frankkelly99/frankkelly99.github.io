#### App.py code

from flask import Flask, render_template, Response, request, redirect, url_for
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html');

def move_forward():
    #Moving forward code
    print("Moving Forward...")