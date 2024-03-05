def b_search(data: list, value: any):
    i = 0
    j = len(data) - 1

    while i < j:
        mid = (i + j) // 2
        if data[mid] == value:
            return mid
        elif data[mid] < value:
            i = mid + 1
        else:
            j = mid - 1
    return None
