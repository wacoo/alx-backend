#!/usr/bin/env python3
''' basic flask app used to start a small localization program '''
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Union

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
    local = g.user.get('locale')
    if local in app.config['LANGUAGES']:
        return local
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def home():
    ''' serves 0-index.html '''
    return render_template('6-index.html')


@app.before_request
def before_request() -> None:
    ''' get user info and assign to g user '''
    user = get_user()
    g.user = user


def get_user() -> Union[str, None]:
    ''' return user data '''
    id = request.args.get('login_as')
    if id:
        return users.get(int(id))
    return None


if __name__ == '__main__':
    app.run()
