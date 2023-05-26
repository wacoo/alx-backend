#!/usr/bin/env python3
''' basic flask app used to start a small localization program '''
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    ''' language and timezone configguration class '''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    BABEL_DEFAULT_LOCALE = 'en'


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@app.route('/')
def home():
    ''' serves 0-index.html '''
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
