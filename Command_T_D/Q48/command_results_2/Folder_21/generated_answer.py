
def return_binary_or_hexa(test_tup):
    res = ""
    a = test_tup[15]
    b = test_tup[57]
    for x in range(a + 1, b):
        if x not in test_tup:
            if (x & 1) == 1:
                res += "1"
            else:
                res += "0"
            x = x >> 1
    return res
