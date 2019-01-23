"""
1/23/2019
"""

__author__ = 'cardinalion'

def is_isbn_or_key(word):
    # isbn isbn13, 13 0~9
    # isbn10, 10 0~9 + '-'
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_word = word.replace('-', '')
    if '-' in word and len(short_word) == 10 and short_word.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key