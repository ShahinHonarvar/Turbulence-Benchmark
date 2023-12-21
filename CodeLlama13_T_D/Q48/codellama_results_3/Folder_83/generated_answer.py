
def return_binary_or_hexa(tup):
    a, b = tup[90], tup[200]
    result = 0
    for i in range(a + 1, b - 1):
        if i not in tup:
            result += i
    if result % 2 == 0:
        return hex(result)[2:]
    else:
        return bin(result)[2:]
