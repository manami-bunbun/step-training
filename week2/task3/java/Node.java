package java;


public class Node {
    String url;
    String webPage;
    Node prev;
    Node next;

    public Node(String url, String webPage){
        this.url = url;
        this.webPage = webPage;
    }
}
