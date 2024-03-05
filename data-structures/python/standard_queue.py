from typing import TypeVar

T = TypeVar("T")


class Node:
    def __init__(self, value: T) -> None:
        self.value = value
        self.next = None


class Queue:
    _front: Node = None
    _back: Node = _front
    _length: int = 0

    def __iter__(self):
        self._current = self._front
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

    def push(self, value: T):
        newNode = Node(value)
        if self._front is None:
            self._front = newNode
            self._back = self._front
        elif self._length == 1:
            self._back = newNode
            self._front.next = self._back
        else:
            self._back.next = newNode
            self._back = self._back.next

        self._length += 1

    def pop(self):
        self._front = self._front.next
        self._length -= 1

    def toString(self):
        current = self._front
        result = "["
        while current.next is not None:
            result += f"{current.value}, "
            current = current.next
        result += f"{current.value}]"
        print(result)

    def front(self):
        return self._front.value if self._length > 0 else None

    def rear(self):
        return self._back.value if self._length > 0 else None

    def empty(self):
        return True if self._length == 0 else False
