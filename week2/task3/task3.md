# Task3
> Design a cache that achieves the following operations with mostly O(1)
> When a pair of <URL, Web page> is given, find if the given pair is contained in the cache or not
> If the pair is not found, insert the pair into the cache after evicting the least recently accessed pair


## Java

```
Node.java - Node class
URLCache.java - Cache implemented
TestURLCache.java - for tests (run this file!) 
```

### URLCache.java

* Double Linked list for the order 
* HashTable for to map url and page
