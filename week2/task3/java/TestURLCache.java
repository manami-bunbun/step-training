package java;


public class TestURLCache {
    public static void main(String[] args) {
        // capacityを3で設定する
        URLCache cache = new URLCache(5);

        System.out.println("================set 5 pages==============");
        cache.set("urlA", "pageA");
        cache.set("urlB", "pageB");
        cache.set("urlC", "pageC");
        cache.set("urlD", "pageD");
        cache.set("urlE", "pageE");

        cache.printCache();
        

        
        assert cache.get("urlA").equals("pageA"); 
        assert cache.get("urlB").equals("pageB"); 
        assert cache.get("urlC").equals("pageC"); 
        assert cache.get("urlD").equals("pageD"); 
        assert cache.get("urlE").equals("pageE"); 
        System.out.println("hash table works\n");

        System.out.println("==============set a new page F=============\n");    
        cache.set("urlF", "pageF");

        cache.printCache();
        assert cache.get("urlA") == null; 
        assert cache.get("urlB").equals("pageB"); 
        assert cache.get("urlC").equals("pageC"); 
        assert cache.get("urlD").equals("pageD"); 
        assert cache.get("urlE").equals("pageE"); 
        assert cache.get("urlF").equals("pageF"); 
        System.out.println("linkedlist works\n");


        System.out.println("==============access page B==============\n");  
        cache.set("urlB", "pageB");  
        System.out.println("cache works\n");

        cache.printCache();

        System.out.println("==============access page E==============\n");  
        cache.set("urlE", "pageE");  
        cache.printCache();

    }
}
