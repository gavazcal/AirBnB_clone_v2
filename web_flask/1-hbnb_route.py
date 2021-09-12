#!/usr/bin/python3
"""
starts Flask
"""


from flask import Flask

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

if __name__ == "__main__":
    app.run(debug=True)

