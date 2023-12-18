#!/usr/bin/python3
"""
flask first exercise
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


def teardown_appcontext(exception=None):
    """_summary_

    Args:
        exception (_type_, optional): _description_. Defaults to None.
    """
    storage.close()


app.teardown_appcontext(teardown_appcontext)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
    Returns:
        city + state list
    """
    states = storage.all(State)
    sorted_states = {state.id: state for state in
                     sorted(states.values(), key=lambda x: x.name)}

    return render_template('8-cities_by_states.html', states=sorted_states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
