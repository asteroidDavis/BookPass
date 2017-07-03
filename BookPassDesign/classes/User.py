import Book

# a data structure representing a user of BookPass
class User:

    def __init__(self):
        # pick default value so the db can be queried in one go
        self.__logged_in = False
        self.__books = []
