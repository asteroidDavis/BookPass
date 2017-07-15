from Page import Page

class Book:

    def __init__(self, uri=None, name=None):
        # name the book
        if name:
            self.name = name
        else:
            self.name = ''
        # how many words are in this book
        self.word_count = 0
        # what word is the book currently positioned at
        self.location = 0
        # what are the important locations in the book
        self.bookmarks = []
        # how many bookmarks are currently in the book
        self.bookmark_count = 0
        # where is the book stored
        if uri:
            self.uri = uri
        else:
            self.uri = ''
        # the words currently in memory
        self.current_page = Page()
        # is the book downloaded yet
        self.check_out = False

    def read_word(self):
        self.current_page.read(self.uri, self.location)
