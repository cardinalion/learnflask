"""
1/21/2019
"""

from flask import Flask

__author__ = 'cardinalion'

app = Flask(__name__)

"""
#another url registration method
app.add_url_rule('/hello',view_func=hello)
#基于类的视图（即插视图）
"""

#'/hello/' redirects to '/hello', with status number 301,302, but doesn't have unique url
#click CLTL + B to go to the source code
#route function also uses app.add_url_rule('',)
@app.route('/hello')
def hello():
    return 'Hello'

#debug mode on，no need to restart server，detailed error info
app.run(debug=True)
