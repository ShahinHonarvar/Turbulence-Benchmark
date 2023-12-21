
def return_binary_or_hexa(test_tup):
    res = 0
    a, b = sorted(test_tup)[427], sorted(test_tup)[669]
    for i in range(a + 1, b - 1):
        if i not in test_tup:
            res += i
    if res % 2:
        return bin(res)[2:]
    else:
        return hex(res)[2:]
