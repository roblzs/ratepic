from flask import Blueprint, render_template, request, flash, redirect, session
from flask.helpers import url_for

home = Blueprint("home", __name__)

scores = open("ratepic/scores.txt", "r")
print(scores.read())

image1 = ""
image2 = ""

@home.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html", image1=image1, image2=image2)

def click_image():
    pass