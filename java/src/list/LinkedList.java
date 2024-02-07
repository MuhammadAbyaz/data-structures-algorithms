package list;

public class LinkedList<T> {

    public static class Node<T> {
        T _data;
        Node<T> next;

        public Node(T data) {
            this.next = null;
            this._data = data;
        }
    }

    int size = 0;
    Node<T> head = null;
    Node<T> tail = null;

    public void add(T data) {
        Node<T> newNode = new Node<>(data);
        if (head == null) {
            head = newNode;
            tail = newNode;
        } else {
            tail.next = newNode;
            tail = newNode;
        }
        size++;
    }

    public String toString() {
        StringBuilder listToString = new StringBuilder();
        Node<T> current = head;
        listToString.append("[");
        while (current.next != null) {
            listToString.append(current._data);
            listToString.append(", ");
            current = current.next;
        }
        listToString.append(tail._data);
        listToString.append("]");
        return listToString.toString();
    }

    public int size() {
        return size;
    }

    public T get(int index) throws IndexOutOfBoundsException, NullPointerException {
        Node<T> current = head;
        for (int i = 0; i < index; i++) {
            current = current.next;
        }
        return current._data;
    }

    public void insert(int index, T data) throws IndexOutOfBoundsException {
        Node<T> current = head;
        Node<T> newNode = new Node<T>(data);
        for (int i = 0; i < index - 1; i++) {
            current = current.next;
        }
        newNode.next = current.next;
        current.next = newNode;
        size++;
    }

    public void remove(int index) {
        Node<T> current = head;
        for (int i = 0; i < index - 1; i++) {
            current = current.next;
        }
        current.next = current.next.next;
        size--;
    }

    public void reverse() {
        Node<T> current = head;
        Node<T> next;
        Node<T> previous = null;

        while (current != null) {
            next = current.next;
            current.next = previous;
            previous = current;
            current = next;
        }
        tail = head;
        head = previous;
    }
}
