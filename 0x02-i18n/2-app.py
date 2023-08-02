#!/usr/bin/env python3
"""A Basic Flask app wuth babel config.
"""
from flask_babel import Babel, request
from flask import Flask, render_template


class Config:
    """class used for flask_babel configuration.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@app.route('/')
def get_index() -> str:
    """The index route.
    """
    return render_template('2-index.html')


@babel.localeselector
def get_locale():
    """This selects the language based on our config"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
