
from sqlalchemy.sql import text
from flask import Flask
from flask import redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/yhteystiedot")
def yhteystiedot():
    return render_template("yhteystiedot.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route("/admin")
def admin():
    return render_template("admin.html")