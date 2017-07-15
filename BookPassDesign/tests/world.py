from BookPassDesign.classes import Book
from lettuce import world

'''
a_long_book() - return an object of the book class with hundreds of pages and fields
'''
#todo: finish this then finish the rest of entries in tests\Page.py
@world.absorb
def a_long_book():
    long_book = Book.Book()
    return long_book
