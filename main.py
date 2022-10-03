from flask import Flask, redirect, url_for, render_template, request, session, flash, send_from_directory
from flask_sqlalchemy import SQLAlchemy
import json
import requests
from py_edamam import PyEdamam
from py_edamam import Edamam
from jinja2 import Template
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

def edamam_search(query):
    app_id = os.environ['7aa51ca1']
    app_key = os.environ['ce12c48568e3a63fa86df26eb277a991']

    curl = f"https://api.edamam.com/search?q={query}"\
            f"&app_id={app_id}"\
            f"&app_key={app_key}"

    response = requests.get(curl)
    hits = response.json()["hits"]

    return hits

@app.route('/recipes')
def search():
    ingredient = request.args.get("ingredient")
    hits = edamam_search(ingredient)

    with open("./templates/recipes.html") as file_:
        template = Template(file_.read())
    return template.render(ingredient=ingredient, hits=hits)

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