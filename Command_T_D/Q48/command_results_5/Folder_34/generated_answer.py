
def return_binary_or_hexa(test_tup):
    a, b = test_tup[60], test_tup[200]
    if a == b - 1:
        return ""
    test_tup = set(test_tup)
    res = test_tup.count(a) + test_tup.count(b - 1)
    if res % 2 == 1:
        return bin(a + b - 1 - res).zfill(len(bin(a + b - 1 - res)))
    else:
        return hex(a + b - 1 - res)
