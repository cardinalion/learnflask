"""
1/23/2019
"""

__author__ = 'cardinalion'

from flask import jsonify
from helper import is_isbn_or_key
from yushu_book import YuShuBook


@app.route('/book/search/<q>/<page>')
def search(query, page):
    """
        query : key word, isbn
        page
    """
    isbn_or_key = is_isbn_or_key(query)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(query)
    else:
        result = YuShuBook.search_by_keyword(query)
        # API
    # return json.dumps(result), 200, {'content-type':'application/json'}
    return jsonify(result)
