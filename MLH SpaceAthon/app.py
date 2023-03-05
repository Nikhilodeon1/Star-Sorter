#this file and everything else in this repository was made by Nikhil | (c) Nikhil 2023
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from roboflow import Roboflow
app = Flask(__name__)
app.secret_key = "|\|||<|-|||_"
rf = Roboflow(api_key="pKy05SQyiUaPlVkNNLlG")
project = rf.workspace().project("star-sorter")
model = project.version(1).model


@app.route('/')
def home():
    return render_template('home.html', msg='')