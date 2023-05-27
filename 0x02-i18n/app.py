#!/usr/bin/env python3
''' basic flask app used to start a small localization program '''
import pytz
import locale
from flask import Flask, render_template, request, g
from flask_babel import Babel, format_datetime
from typing import Union
from pytz import timezone
from datetime import datetime
import pytz.exceptions

app = Flask(__name__)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    ''' language and timezone configguration class '''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    BABEL_DEFAULT_LOCALE = 'en'


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    ''' select locale '''
    locale = request.args.get('locale', '')
    cfg = app.config["LANGUAGES"]

    if locale in cfg:
        return locale
    if g.user and g.user['locale'] in cfg:
        return g.user['locale']
    header_locale = request.headers.get('locale', '')
    if header_locale in cfg:
        return header_locale
    return request.accept_languages.best_match(cfg)


@babel.timezoneselector
def get_timezone() -> Union[str, None]:
    ''' returns timezone '''
    default = app.config["BABEL_DEFAULT_TIMEZONE"]
    try:
        tz = request.args.get('timezone', '')
        if tz:
            timez = pytz.timezone(tz)
            return timez.zone
        if g.user and g.user['timezone']:
            timez = pytz.timezone(g.user['timezone'])
            return timez.zone
        return default
    except pytz.exceptions.UnknownTimeZoneError:
        return default


@app.route('/', strict_slashes=False)
def home():
    ''' serves 0-index.html '''
    return render_template('7-index.html')


@app.before_request
def before_request() -> None:
    ''' get user info and assign to g user '''
    user = get_user()
    g.user = user
    current_time = pytz.utc.localize(datetime.utcnow())
    time = current_time.astimezone(timezone(get_timezone()))
    locale.setlocale(locale.LC_TIME, (get_locale(), 'UTF-8'))
    format = '%b %d, %Y %I:%M:%S %p'
    g.time = time.strftime(format)


def get_user() -> Union[str, None]:
    ''' return user data '''
    id = request.args.get('login_as')
    if id:
        return users.get(int(id))
    return None


if __name__ == '__main__':
    app.run()
