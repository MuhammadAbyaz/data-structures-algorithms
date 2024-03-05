from typing import TypeVar

T = TypeVar("T")


class Node:
    def __init__(self, value: T):
        self.value = value
        self.next = None
        self.previous = None


class DoublyLinkedList:
    _head: Node = None
    _tail: Node = _head
    _length: int = 0

    def __len__(self):
        return self._length

    def size(self):
        return self._length

    def __iter__(self):
        self._current = self._head
        self._index = -1
        return self

    def __next__(self):
        if self._index < self._length - 1:
            data = self._current.value
            self._current = self._current.next
            self._index += 1
            return data
        else:
            raise StopIteration

    def append(self, value: T):
        newNode = Node(value)
        if self._head == None:
            self._head = newNode
            self._tail = self._head
        else:
            self._tail.next = newNode
            newNode.previous = self._tail
            self._tail = self._tail.next
        self._length += 1

    def pop(self):
        self._tail = self._tail.previous
        self._tail.next = None

    def remove(self, index):
        if index == 0:
            self._head = self._head.next
            self._head.previous = None
        else:
            current = self._head
            for _ in range(0, index - 1):
                current = current.next
            current.next = current.next.next
        self._length -= 1

    def reverse(self):
        current = self._head
        temp = current.next
        while temp is not None:
            current.previous, current.next = current.next, current.previous
            current = temp
            temp = current.next
        current.previous, current.next = current.next, current.previous
        self._tail.previous = None
        self._head, self._tail = self._tail, self._head

    def indexOf(self, value: T):
        current = self._head
        index = 0
        if current.value == value:
            return index
        else:
            while current.next is not None:
                if current.value == value:
                    return index
                current = current.next
                index += 1
            return index if self._tail.value == value else -1

    def toString(self):
        current = self._head
        result = "["
        while current.next is not None:
            result += f"{current.value}, "
            current = current.next
        result += f"{current.value}]"
        print(result)
