# main.py

from flask import render_template
from app import app

@app.route('/')
def index():
    return render_template('index.html')

def greet(name):
    return "Hello, " + name

if __name__ == "__main__":
    app.run(debug=True)
