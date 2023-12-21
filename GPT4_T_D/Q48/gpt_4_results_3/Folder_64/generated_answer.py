
def return_binary_or_hexa(tup):
    a = tup[0]
    b = tup[5]
    res = sum(set(range(a + 1, b)) - set(tup[1:5]))
    if res % 2 == 0:
        return hex(res)[2:]
    else:
        return bin(res)[2:]
