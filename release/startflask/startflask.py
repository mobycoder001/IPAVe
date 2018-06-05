#!/usr/bin/env python3


from flask import Flask
app = Flask(__name__)


@app.route('/')
def ipave_index():
    return title_redirect()

def title_redirect():
    html_redirect='<html><head><title>Hello Three</title><meta http-equiv="refresh" content="0;URL=../static/index.html"> \
        </head><body><h4>formatted h4</h4></body></html>'
    return html_redirect

@app.route('/static')
def something():
    return url_for('static', filename='index.html')

#notes: https:// vsupalov.com/flask-web-server-in-production/ don't do it, see WSGI

if __name__ == '__main__':
    app.run()
