class Page:

    def __init__(self):
        self.max_lines = 64
        self.lines = 0
        self.__words = []

    '''
    read_page(self, path, offset) - fill words with the contents of the uri
    PARAMS:
        path: location to read the page from
        offset: how far into the page to start fetching the page
    '''
    def read_page(self, path, offset):
        # open the book for reading
        with open(path, 'r') as fid:
            # read the entire book into memory Todo: make this read from the offset to offset plus lines
            lines = fid.readlines()
            self.lines = len(lines[offset:])
            self.__words = lines[offset:offset+self.lines]

    def is_empty(self):
        return(len(self.__words) > 0)
