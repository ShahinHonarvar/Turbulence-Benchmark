
def return_binary_or_hexa(tup):
    a = tup[90]
    b = tup[200]
    sum = 0
    for i in range(a + 1, b - 1):
        if not (i in tup):
            sum += i
    if sum % 2 == 0:
        return hex(sum)[2:]
    else:
        return bin(sum)[2:]
