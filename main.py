# -*- coding: utf-8 -*-
from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about')
def redpanda():
    return redirect(render_template("RedPanda.html"))

if __name__ == "__main__":
    app.run()