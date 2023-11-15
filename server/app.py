#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Welcome to the Home Page!</h1>'

@app.route('/<username>')
def user(username):
    return f'<h1> This is {username}\'s profile. </h1>'

if __name__ == '__main__':
    app.run(debug=True)