def badd(num1: str, num2: str):
    c = 0
    s = ""
    for i in range(1, len(num1) + 1):
        d = (int(num1[-i]) + int(num2[-i]) + c) // 2
        s += str((int(num1[-i]) + int(num2[-i]) + c) % 2)
        c = d
    s += str(c)
    return s[::-1]


print(badd("1001", "1111"))
