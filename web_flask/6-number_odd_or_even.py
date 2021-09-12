#!/usr/bin/python3
"""
starts Flask
"""


from flask import Flask
from flask import render_template


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

@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python_print(text):
    """Prints python with variable text"""
    if len(text) > 0:
        text = text.replace("_", " ")
    return "Python {}".format(text)

@app.route('/number/<int:n>')
def number(n):
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def html(n):
    """HTML template"""
    return render_template('5-number.html', n=n)

@app.route('/number_odd_or_even/<int:n>')
def even_or_odd(n):
    """Displays HTML"""
    return render_template('6-number_odd_or_even.html', n=n)

if __name__ == "__main__":
    app.run(debug=True)

