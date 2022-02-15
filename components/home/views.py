from flask import Blueprint, render_template, request, flash, redirect, session
from flask.helpers import url_for

home = Blueprint("home", __name__)


@home.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")
        