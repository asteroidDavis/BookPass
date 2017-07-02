

class Book:

    def __init__(self):
        # how many words are in this book
        self.__word_count = 0
        # what word is the book currently positioned at
        self.__location = ''
        # what are the important locations in the book
        self.__bookmarks = []
        # how many bookmarks are currently in the book
        self.__bookmark_count = 0
        # where is the book stored
        self.__uri = ''
        # the words currently in memory
        self.__current_page = ""
        # how many words to store in memory at a time
        self.__page_size = 1024
        # todo: add a custom font for each book

    def read_word(self):
        pass