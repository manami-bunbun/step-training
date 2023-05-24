class Node:
    def __init__(self, url, webPage):
        self.url = url
        self.webPage = webPage
        self.prev = None
        self.next = None
