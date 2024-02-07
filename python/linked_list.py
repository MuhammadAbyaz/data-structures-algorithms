from typing import TypeVar

T = TypeVar("T")


class Node:
    def __init__(self, value: T):
        self.value = value
        self.next = None


class LinkedList:
    _head: Node = None
    _tail: Node = _head
    _length: int = 0

    def __len__(self):
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

    def size(self):
        return self._length

    def append(self, value: T):
        newNode = Node(value)
        if self._head is None:
            self._head = newNode
            self._tail = self._head
        else:
            self._tail.next = newNode
            self._tail = self._tail.next
        self._length += 1

    def pop(self):
        current = self._head
        while current.next.next is not None:
            current = current.next
        self._tail = current
        self._tail.next = None

    def remove(self, index: int):
        if index == 0:
            self._head = self._head.next
        else:
            current = self._head
            for _ in range(0, index - 1):
                current = current.next
            current.next = current.next.next
        self._length -= 1

    def reverse(self):
        previous = self._head
        current = self._head
        next = current.next

        while current.next is not None:
            if current == self._head:
                current.next = None
                current = next
            else:
                current.next = previous
                previous = current
                current = next
            next = current.next
        self._tail.next = previous
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

    def isEmpty(self):
        return True if self._length == 0 else False
