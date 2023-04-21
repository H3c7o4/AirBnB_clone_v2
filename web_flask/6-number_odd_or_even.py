#!/usr/bin/python3
"""
Script that starts a Flask web application:
    - Listen on port 5000 with local host 0.0.0.0
    - display "Hello  HBNB" on route /
    - display "HBNB" on route /hbnb
    - display “C ” followed by the value of the
      text variable on route /c/<text>
    - display “n is a number” only if n is an integer on route /number/<n>
    - display “Python ”, followed by the value of the text
      variable on route /python/(<text>)
    - display a HTML page only if n is an integer on route /number_template/<n>
"""
from flask import Flask, render_template

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


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_something(text="is_cool"):
    """ Function that returns the message "python"
    followed by the value of the text  on a web browser
    """
    text = text.replace("_", " ")
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    """ Function that returns the message "python"
    followed by the value of the text  on a web browser
    """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def is_number_template(n):
    """ Function that returns the message "python"
    followed by the value of the text  on a web browser
    """
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def is_even_or_odd_number(n):
    """ Function that returns the message "python"
    followed by the value of the text  on a web browser
    """
    even = "even"
    odd = "odd"
    if n % 2 == 0:
        return render_template('6-number_odd_or_even.html', number=n,
                               pair=even)
    else:
        return render_template('6-number_odd_or_even.html', number=n,
                               pair=odd)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
