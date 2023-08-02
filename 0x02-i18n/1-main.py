#!/usr/bin/env python3
"""A Basic Flask app with babel config.
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config(object):
    """creates configurations for the flask app
    """
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    LANGUAGES = ['en', 'fr']


app = Flask(__name__)
app.url_map.strict_slashes = False
bable = Babel(app)
app.config.from_object(Config)


@app.route('/')
def get_index() -> str:
    """The index route.
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
