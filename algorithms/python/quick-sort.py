def qs(arr: list[int], lo: int, hi: int):
    if lo >= hi:
        return
    pivotIdx = partition(arr, lo, hi)
    qs(arr, lo, pivotIdx - 1)
    qs(arr, pivotIdx + 1, hi)


def partition(arr: list[int], lo: int, hi: int) -> int:
    pivot = arr[hi]
    idx = lo - 1
    for i in range(lo, hi):
        if arr[i] <= arr[pivot]:
            idx += 1
            arr[i], arr[idx] = arr[idx], arr[i]
    idx += 1
    arr[idx], pivot = pivot, arr[idx]
    return idx


def quick_sort(arr: list[int]):
    qs(arr, 0, len(arr) - 1)
