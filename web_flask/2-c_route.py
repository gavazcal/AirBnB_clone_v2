#!/usr/bin/python3
"""
starts Flask
"""


from flask import Flask
import sys


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """Prints output"""
    return "Hello HBNB!"

@app.route('/hbnb')
def helloagain():
    """Other hello"""
    return "HBNB"

@app.route('/c/<text>')
def c_print(text):
    """Print out c with variable text"""
    text = text.replace("_", " ")
    return "C {}".format(text)

if __name__ == "__main__":
    app.run(debug=True)
