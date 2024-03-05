def isort(data: list):
    for i in range(len(data)):
        temp = data[i]
        j = i - 1
        while j >= 0 and temp < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = temp
    return data
