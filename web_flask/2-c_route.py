#!/usr/bin/python3
"""
Script that starts a Flask web application:
    Listen on port 5000 with local host 0.0.0.0
    display "Hello  HBNB" on route /
    display "HBNB" on route /hbnb
    display “C ” followed by the value of the text variable on route /c/<text>
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


@app.route('/c/<text>', strict_slashes=False)
def C_is_something(text):
    """ Function that returns the message "C"
    followed by the value of the text  on a web browser
    """
    text = text.replace("_", " ")
    return 'C {}'.format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
