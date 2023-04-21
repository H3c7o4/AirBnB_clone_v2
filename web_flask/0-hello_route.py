#!/usr/bin/python3
# script that starts a Flask web application:
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """ Function that returns a message on a web browser """
    return 'Hello HBNB!'
