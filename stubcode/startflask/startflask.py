#!/usr/bin/env python3


from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

@app.route('/hellotoo/')
def hello_too():
    return render_hello_too()

def render_hello_too():
    return "Hello Too!"

@app.route('/hello3/')
def hello3():
    return render_hello_3()

def render_hello_3():
   html_stuff="<html><head><title>Hello Three</title><body><h4>formatted h4</h4></body></html>"
   return html_stuff

#fails
#@app.route('/other')
#def other():
#    return url_for('other', filename='index.html')
#    return url_for('static', filename='index.html')

@app.route('/static')
def something():
    return url_for('static', filename='test.html')

#also works (renders url: http://x.x.x.x:5000/static/test001.html
#also works (renders url: http://x.x.x.x:5000/static/test4.html
#@app.route('/static')
#def root():
#    return app.send_static_file('test001.html')

### works below
#@app.route('/static')
#def root():
#    return url_for('static', filename='test3.html')

#notes: https:// vsupalov.com/flask-web-server-in-production/ don't do it, see WSGI

if __name__ == '__main__':
    app.run()
