from node import Node

class URLCache:
    def __init__(self,capacity):
       self.capacity = capacity
       self.map ={}
       self.head = None
       self.tail = None
    
    def get(self,url):
        if url in self.map:
            node = self.map[url]
            self.remove(node)
            self.setHead(node)
            return node.webPage
        else:
            return None
    
    def set(self, url, webPage):
        if url in self.map:
            node = self.map[url]
            node.webPage = webPage
            self.remove(node)
            self.setHead(node)
        else:
            node = Node(url,webPage)
            if len(self.map) >= self.capacity:
                del self.map[self.tail.url]
                self.remove(self.tail)
                self.setHead(node)
            else:
                self.setHead(node)
            self.map[url] = node
    
    def remove(self, node):
        if(node.prev != None):
            node.prev.next = node.next
        else:
            self.head = node.next
            
        if(node.next != None):
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        
    
    def setHead(self, node):
        node.next = self.head
        node.prev = None
        
        if self.head != None:
            self.head.prev = node
        
        head = node
        
        if self.tail == None:
            self.tail = self.head
            
    def printCache(self):
        currentNode = self.head 
        while currentNode != None:
            print([currentNode.url,currentNode.webPage])
            currentNode = currentNode.next
            if currentNode != None:
                print("->")
        print("\n")
        
