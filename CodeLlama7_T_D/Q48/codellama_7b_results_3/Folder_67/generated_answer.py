
def return_binary_or_hexa(tuple):
    a = tuple[44]
    b = tuple[67]
    sum = 0

    for i in range(a + 1, b - 1 + 1):
        if not (i in tuple[44:67 + 1]):
            sum += i

    if sum % 2 == 0:
        return hex(sum)[2:]

    else:
        return bin(sum)[3:]
