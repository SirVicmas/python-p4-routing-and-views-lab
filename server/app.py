#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:text>')
def print_screen(text):
    print(text)
    return f"<p>String printed: {text}</p>"

@app.route('/count/<int:num>')
def count(num):
    if num < 1:
        return "Please provide a positive integer."
    
    numbers = "\n".join(str(i) for i in range(1, num + 1))
    return f"<pre>{numbers}</pre>"


if __name__ == '__main__':
    app.run(port=5555, debug=True)
