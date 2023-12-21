
def return_binary_or_hexa(test_tup):
    res = ""
    a, b = test_tup[44], test_tup[78]
    res = sum(x for x in range(a + 1, b))
    if res % 2 == 1:
        return bin(res).zfill(len(bin(res)) - 2)
    return hex(res)[2:]
