def custom_max(data: list):
    max_number = data[0]
    for i in range(1, len(data)):
        if max_number < data[i]:
            max_number = data[i]
    return max_number
