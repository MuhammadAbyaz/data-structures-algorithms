from typing import TypeVar

T = TypeVar("T")


class Node:
    def __init__(self, value: T):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self) -> None:
        self._bstNode: Node = None

    def insert(self, value: T, **kwargs):
        if len(kwargs) == 0:
            root = self._bstNode
        else:
            root = kwargs["input_root"]
        if self._bstNode is None:
            newNode = Node(value)
            self._bstNode = newNode
        if root is None:
            newNode = Node(value)
            root = newNode
        elif value <= root.value:
            root.left = self.insert(value, input_root=root.left)
        else:
            root.right = self.insert(value, input_root=root.right)
        return root

    def search(self, value: T, **kwargs):
        if self._bstNode is None:
            return -1
        if len(kwargs) == 0:
            root = self._bstNode
        else:
            root = kwargs["input_root"]
        if root is None:
            return False
        elif root.value == value:
            return True
        elif value < root.value:
            return self.search(value, input_root=root.left)
        else:
            return self.search(value, input_root=root.right)

    def max(self, **kwargs):
        if self._bstNode is None:
            return -1
        if len(kwargs) == 0:
            root = self._bstNode
        else:
            root = kwargs["input_root"]
        if root.right is None:
            return root.value
        return self.max(input_root=root.right)

    def min(self, **kwargs):
        if self._bstNode is None:
            return -1
        if len(kwargs) == 0:
            root = self._bstNode
        else:
            root = kwargs["input_root"]
        if root.left is None:
            return root.value
        return self.min(input_root=root.left)

    def find_height(self, **kwargs):
        if len(kwargs) == 0:
            root = self._bstNode
        else:
            root = kwargs["input_root"]
        if root is None:
            return -1
        left = self.find_height(input_root=root.left)
        right = self.find_height(input_root=root.right)
        return max(left, right) + 1
