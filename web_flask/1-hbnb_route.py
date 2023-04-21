#!/usr/bin/python3
"""
script that starts a Flask web application that:
     listen on port 0.0.0.0
     display "Hello  HBNB" on route /
     display "HBNB" on route /hbnb
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """ Function that returns a message on a web browser """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """ Function that returns the message "HBNB" on a web browser """
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
