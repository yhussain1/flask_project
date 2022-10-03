from flask import Flask, redirect, url_for, render_template, request, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/Breakfast")
def breakfast():
    return render_template("breakfast.html")

@app.route("/Lunch")
def lunch():
    return render_template("lunch.html")

@app.route("/Dinner")
def dinner():
    return render_template("dinner.html")

if __name__ == "__main__":
    app.run(debug=True)