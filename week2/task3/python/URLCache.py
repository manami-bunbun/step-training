from node import Node

class URLCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.map = {}
        self.head = None
        self.tail = None

    def get(self, url):
        if url in self.map:
            node = self.map[url]
            self.remove(node)
            self.setHead(node)
            return node.webPage
        return None

    def set(self, url, webPage):
        if url in self.map:
            old = self.map[url]
            old.webPage = webPage
            self.remove(old)
            self.setHead(old)
        else:
            created = Node(url, webPage)
            if len(self.map) >= self.capacity:
                del self.map[self.tail.url]
                self.remove(self.tail)
                self.setHead(created)
            else:
                self.setHead(created)
            self.map[url] = created

    def remove(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next is not None:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

    def setHead(self, node):
        node.next = self.head
        node.prev = None

        if self.head is not None:
            self.head.prev = node

        self.head = node

        if self.tail is None:
            self.tail = self.head

    def printCache(self):
        currentNode = self.head
        while currentNode is not None:
            print(f"[{currentNode.url}, {currentNode.webPage}]", end="")
            currentNode = currentNode.next
            if currentNode is not None:
                print(" -> ", end="")
        print()
