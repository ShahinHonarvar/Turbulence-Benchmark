
def return_binary_or_hexa(test_tup):
    res = ""
    a, b = test_tup[3], test_tup[8]
    if a <= b - 1:
        res = test_tup[a + 1:b - 1]
    else:
        res = test_tup[a + 1:]
    if res.count("0") % 2:
        res = bin(sum(res))
    else:
        res = hex(sum(res))
    return res
