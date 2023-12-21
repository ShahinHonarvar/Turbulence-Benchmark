
def return_binary_or_hexa(test_tup):
    res = ""
    a, b = test_tup[6], test_tup[7]
    for i in range(a + 1, b - 1):
        if i not in test_tup:
            if i % 2 == 1:
                res += str(i)
            else:
                res += hex(i)
    return res
