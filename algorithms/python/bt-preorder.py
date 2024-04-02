class BinaryNode:
    def __init__(self) -> None:
        self.value: int
        self.left: BinaryNode
        self.right: BinaryNode


def walk(curr: BinaryNode | None, path: list[int]) -> list[int]:
    if not curr:
        return path
    path.append(curr.value)
    walk(curr.left, path)
    walk(curr.right, path)
    return path


def pre_order_search(head: BinaryNode) -> list[int]:
    return walk(head, [])
