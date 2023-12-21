
def return_binary_or_hexa(tup):
    a, b = 20, 200
    res = sum(x for x in range(a + 1, b - 1) if x not in tup)
    if res % 2 == 1:
        return bin(res)[2:]
    else:
        return hex(res)[2:]
