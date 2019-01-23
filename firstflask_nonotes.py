"""
1/21/2019
"""

from flask import Flask

__author__ = 'cardinalion'

app = Flask(__name__)
app.config.from_object('config')

@app.route('/hello')
def hello():
    return 'Hello'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=81)
