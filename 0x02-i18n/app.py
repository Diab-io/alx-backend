#!/usr/bin/env python3
"""A Basic Flask app wuth babel config.
"""
from flask_babel import Babel, request, format_datetime
from flask import Flask, render_template, g
import pytz


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
        if user_id:
            user_id = int(user_id)
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
    g.time = format_datetime()
    return render_template('index.html')


@babel.localeselector
def get_locale():
    """This selects the language based on our config"""
    url_query = request.args.get('locale')
    if url_query in app.config['LANGUAGES']:
        return url_query
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']
    locale_from_header = request.headers.get('locale')
    if locale_from_header in app.config['LANGUAGES']:
        return locale_from_header
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """This selects the language based on our timezone"""
    timezone = request.args.get('timezone')
    if g.user and not timezone:
        timezone = g.user['timezone']
    try:
        return pytz.timezone(timezone).zone
    except pytz.UnknownTimeZoneError:
        return app.config['BABEL_DEFAULT_TIMEZONE']


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
