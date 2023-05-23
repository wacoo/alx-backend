#!/usr/bin/env python3
''' basic flask app used to start a small localization program '''
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    ''' render homepage '''
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
