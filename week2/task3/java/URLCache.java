package java;
import java.util.HashMap;

// LRU(Least Recently Used)
public class URLCache {
    private final int capacity;
    private HashMap<String, Node> map;
    private Node head;
    private Node tail;

    public URLCache(int capacity) {
        this.capacity = capacity;
        map = new HashMap<>();
    }

    public String get(String url) {
        if (map.containsKey(url)) {
            Node node = map.get(url);
            remove(node);
            setHead(node);
            return node.webPage;
        }
        return null;
    }

    public void set(String url, String webPage) {
        if (map.containsKey(url)) {
            Node old = map.get(url);
            old.webPage = webPage;
            remove(old);
            setHead(old);
        } else {
            Node created = new Node(url, webPage);
            if (map.size() >= capacity) {
                map.remove(tail.url);
                remove(tail);
                setHead(created);
            } else {
                setHead(created);
            }
            map.put(url, created);
        }
    }

    private void remove(Node node) {
        if (node.prev != null) {
            node.prev.next = node.next;
        } else {
            head = node.next;
        }

        if (node.next != null) {
            node.next.prev = node.prev;
        } else {
            tail = node.prev;
        }
    }

    private void setHead(Node node) {
        node.next = head;
        node.prev = null;

        if (head != null) {
            head.prev = node;
        }

        head = node;

        if (tail == null) {
            tail = head;
        }
    }

    public void printCache() {
        Node currentNode = head;
        while(currentNode != null) {
            System.out.print("[" + currentNode.url + ", " + currentNode.webPage + "]");
            currentNode = currentNode.next;
            if (currentNode != null) {
                System.out.print(" -> ");
            }
        }
        System.out.println();
    }
}
