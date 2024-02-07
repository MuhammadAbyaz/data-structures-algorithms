package list;

import java.util.Iterator;
import java.util.Spliterator;
import java.util.function.Consumer;

public class DoublyLinkedList<T> implements Iterable<T> {

    Node<T> head = null;
    Node<T> tail = null;
    int size = 0;


    private static class Node<T> {
        T value;
        Node<T> next;
        Node<T> previous;

        public Node(T data) {
            this.next = null;
            this.previous = null;
            this.value = data;
        }
    }

    public int size() {
        return size;
    }

    public void addFirst(T value) {
        Node<T> newNode = new Node<>(value);
        newNode.previous = head.previous;
        newNode.next = head;
        head = newNode;
    }

    public void addLast(T value) {
        Node<T> newNode = new Node<>(value);

        if (size == 0) {
            head = newNode;
            tail = newNode;
        } else {
            tail.next = newNode;
            newNode.previous = tail;
            tail = newNode;
        }
        size++;
    }


    public void add(T value) {
        addLast(value);
    }

    public void addAt(int index, T value) throws NullPointerException, IndexOutOfBoundsException {
        Node<T> newNode = new Node<>(value);
        Node<T> current = head;
        for (int i = 0; i < index - 1; i++) {
            current = current.next;
        }
        newNode.next = current.next;
        current.next = newNode;
        newNode.previous = current;
        size++;
    }

    public void get(int index) throws NullPointerException, IndexOutOfBoundsException {
        Node<T> current = head;
        for (int i = 0; i < index; i++) {
            current = current.next;
        }
        System.out.println(current.value);
    }

    public String toString() {
        StringBuilder output = new StringBuilder();
        output.append("[");
        Node<T> current = head;
        while (current.next != null) {
            output.append(current.value);
            output.append(", ");
            current = current.next;
        }
        output.append(tail.value);
        output.append("]");
        return output.toString();
    }

    public String reverse() {
        Node<T> header = head;
        head = tail;
        tail = header;
        StringBuilder output = new StringBuilder();
        output.append("[");
        Node<T> current = head;
        while (current.previous != null) {
            output.append(current.value);
            output.append(", ");
            current = current.previous;
        }
        output.append(tail.value);
        output.append("]");
        return output.toString();
    }


    @Override
    public Iterator<T> iterator() {
        return null;
    }

    @Override
    public void forEach(Consumer<? super T> action) {
        Iterable.super.forEach(action);
    }

    @Override
    public Spliterator<T> spliterator() {
        return Iterable.super.spliterator();
    }
}
