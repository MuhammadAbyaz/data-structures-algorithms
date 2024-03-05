def custom_min(data: list):
    min_number = data[0]
    for i in range(1, len(data)):
        if min_number > data[i]:
            min_number = data[i]
    return min_number
