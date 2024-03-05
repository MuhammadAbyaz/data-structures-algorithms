from typing import TypeVar

T = TypeVar("T")


class Node:
    def __init__(self, value: T):
        self.value = value
        self.next: Node = None


class Stack:
    _top: Node = None
    _length: int = 0

    def __iter__(self):
        self._current = self._top
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

    def push(self, value: T):
        newNode = Node(value)
        temp = self._top
        self._top = newNode
        self._top.next = temp
        self._length += 1

    def pop(self):
        self._top = self._top.next
        self._length -= 1

    def peek(self):
        return self._top.value

    def toString(self):
        result = "["
        current = self._top
        while current.next is not None:
            result += f"{current.value}, "
            current = current.next
        result += f"{current.value}]"
        print(result)

    def empty(self):
        return True if self._length == 0 else False
