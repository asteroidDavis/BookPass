class Page:

    def __init__(self):
        self.max_size = 1024
        self.size = 0
        self.__words = []

    '''
    read_page(self, path, offset) - fill words with the contents of the uri
    PARAMS:
        path: location to read the page from
        offset: how far into the page to start fetching the page
    '''
    def read_page(self, path, offset):
        with open(path) as fid:
            pass

    def is_empty(self):
        return(len(self.__words) > 0)
