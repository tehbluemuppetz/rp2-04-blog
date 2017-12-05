
# blog.py - Controller

# Imports
from flask import Flask, render_template, request, session, \
    flash, redirect, url_for, g

import sqlite3

# Configuration
DATABASE = 'blog.db'

app = Flask(__name__)

# Pulls in app configuration by looking for UPPERCASE variables
app.config.from_object(__name__)

# Function used for connecting to the DB
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/main')
def main():
    return render_template('main.html')


if __name__ == '__main__':
    app.run(debug=True)
