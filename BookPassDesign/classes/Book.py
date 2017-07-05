from Page import Page

class Book:

    def __init__(self):
        # how many words are in this book
        self.__word_count = 0
        # what word is the book currently positioned at
        self.__location = 0
        # what are the important locations in the book
        self.__bookmarks = []
        # how many bookmarks are currently in the book
        self.__bookmark_count = 0
        # where is the book stored
        self.__uri = ''
        # the words currently in memory
        self.__current_page = Page()


    def read_word(self):
        self.__current_page.read(self.__uri, self.__location)
