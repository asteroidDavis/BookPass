import Book
import User

# a data structure representing a user of BookPass
class Reader(User):

    def __init__(self):
        # pick default value so the db can be queried in one go
        self.books = []
