class BinaryNode:
    def __init__(self) -> None:
        self.value: int
        self.left: BinaryNode
        self.right: BinaryNode


def walk(curr: BinaryNode | None, path: list[int]) -> list[int]:
    if not curr:
        return path
    walk(curr.left, path)
    path.append(curr.value)
    walk(curr.right, path)
    return path


def inorder_search(head: BinaryNode) -> list[int]:
    return walk(head, [])
