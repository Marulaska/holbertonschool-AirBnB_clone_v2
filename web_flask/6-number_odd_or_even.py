#!/usr/bin/python3
"""
flask first exercise
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Returns:
        Hello HBNB
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Returns:
        HBNB
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def print_text(text):
    """
    Returns:
        f format, c text
    """
    return f'C {text}'.replace('_', ' ')


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def print_txt(text='is_cool'):
    """
    Returns:
        f format, c text
    """
    return "Python " + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    Returns:
        n: int
    """
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Args:
        n: int
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    Args:
        n: int
    """
    a = "even" if n % 2 == 0 else "odd"
    return render_template('6-number_odd_or_even.html', n=n, a=a)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
