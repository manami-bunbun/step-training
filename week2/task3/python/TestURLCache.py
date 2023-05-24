from URLCache import URLCache
from node import Node


class TestURLCache:
    def main():
        
        cache = URLCache(5)
        
        print("================set 5 pages==============")
        cache.set("urlA", "pageA")
        cache.set("urlB", "pageB")
        cache.set("urlC", "pageC")
        cache.set("urlD", "pageD")
        cache.set("urlE", "pageE")
        
        cache.printCache()
        
        assert cache.get("urlA")==("pageA") 
        assert cache.get("urlB")==("pageB") 
        assert cache.get("urlC")==("pageC") 
        assert cache.get("urlD")==("pageD") 
        assert cache.get("urlE")==("pageE") 
        print("hash table works\n")

        print("==============set a new page F=============\n")    
        cache.set("urlF", "pageF")

        cache.printCache()
        assert cache.get("urlA") == None
        assert cache.get("urlB")==("pageB") 
        assert cache.get("urlC")==("pageC") 
        assert cache.get("urlD")==("pageD") 
        assert cache.get("urlE")==("pageE") 
        assert cache.get("urlF")==("pageF") 
        print("linkedlist works\n")


        print("==============access page B==============\n")  
        cache.set("urlB", "pageB")  
        print("cache works\n")

        cache.printCache()

        print("==============access page E==============\n")  
        cache.set("urlE", "pageE")  
        cache.printCache()


if __name__ == "__main__":
    TestURLCache.main()
