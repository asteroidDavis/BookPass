class Page:

    def __init__(self):
        self.size = 1024
        self.__words = []

    '''
    read_page(self, path, offset) - fill words with the contents of the uri
    PARAMS:
        path: location to read the page from
        offset: how far into the page to start fetching the page
    '''
    def read_page(self, path, offset):
        try:
            fid = open(file=path)
            result = fid.read(self.size)
        finally:
            if fid:
                fid.close()
