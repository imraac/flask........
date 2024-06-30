from flask import Flask

app = Flask (__name__)
# base/index/root route
@app.route('/')
def hello():
    return "Hello World!"

@app.route('/about')
def about():
    return "About Page"

@app.route('/contact')
def contact():
    return "Contact Page"

