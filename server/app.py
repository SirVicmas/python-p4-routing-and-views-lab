#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:text>')
def print_string(text):
    print(text)
    return text

@app.route('/count/<int:parameter>')
def count(parameter):
    count = f''
    for n in range(parameter):
        count += f"{n}\n"
    return count


@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1,operation,num2):
    if operation == "+":
        return str(num1+num2)
    elif operation == "-":
        return str(num1-num2)
    elif operation == '*':
        return str(num1 * num2)
    elif operation == 'div':
        return str(num1/num2)
    elif operation== '%':
        return str(num1%num2)
    else:
        return 'Operation not recognized'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
