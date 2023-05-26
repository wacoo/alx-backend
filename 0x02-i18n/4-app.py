#!/usr/bin/env python3
''' basic flask app used to start a small localization program '''
from flask import Flask, render_template, request
from flask_babel import Babel
from flask_babel import _
from flask_babel import gettext as _l

app = Flask(__name__)


class Config:
    ''' language and timezone configguration class '''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    BABEL_DEFAULT_LOCALE = 'en'


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    return 'fr'#request.accept_languages.best_match(app.config(['LANGUAGES']))


@app.route('/')
def home():
    ''' serves 0-index.html '''
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run()
