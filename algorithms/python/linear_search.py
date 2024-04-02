from typing import TypeVar

T = TypeVar("T")


def l_search(data: list, value: T):
    for i in range(len(data)):
        if data[i] == value:
            return i
    return None
