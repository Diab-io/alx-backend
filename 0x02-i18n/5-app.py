#!/usr/bin/env python3
"""A Basic Flask app wuth babel config.
"""
from flask_babel import Babel, request
from flask import Flask, render_template, g


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


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """
    This function is used to get the user
    from out mocked login system
    """
    user_id = request.args.get('login_as')
    try:
        user_id = int(user_id)
        if user_id:
            return users[user_id]
    except (KeyError, ValueError):
        return None


@app.before_request
def before_request():
    """
    used to carry out some functionalities before
    request
    """
    user = get_user()
    g.user = user


@app.route('/')
def get_index() -> str:
    """The index route.
    """
    return render_template('5-index.html')


@babel.localeselector
def get_locale():
    """This selects the language based on our config"""
    url_query = request.args.get('locale')
    if url_query in app.config['LANGUAGES']:
        return url_query
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
