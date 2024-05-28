from flask import Flask, request
from ops import *

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/add', methods=['GET'])
def add():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        return str(opsadd(a,b))
    except (TypeError, ValueError):
        return "Invalid input. Please provide two numbers.", 400

@app.route('/subtract', methods=['GET'])
def subtract():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        return str(opssubtract(a,b))
    except (TypeError, ValueError):
        return "Invalid input. Please provide two numbers.", 400

@app.route('/multiply', methods=['GET'])
def multiply():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        return str(opsmultiply(a,b))
    except (TypeError, ValueError):
        return "Invalid input. Please provide two numbers.", 400

@app.route('/divide', methods=['GET'])
def divide():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        if b == 0:
            return "Division by zero is not allowed.", 400
        return str(opsdivide(a,b))
    except (TypeError, ValueError):
        return "Invalid input. Please provide two numbers.", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3030)
