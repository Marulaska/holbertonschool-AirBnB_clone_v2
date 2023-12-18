#!/usr/bin/python3
"""
flask first exercise
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


def teardown_method(exception=None):
    """_summary_

    Args:
        exception (_type_, optional): _description_. Defaults to None.
    """
    storage.close()


@app.teardown_appcontext(teardown_method)
@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    Returns:
        Hello HBNB
    """
    states = storage.all(State)
    storage.close()
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
