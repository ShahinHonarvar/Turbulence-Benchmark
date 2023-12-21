
def return_binary_or_hexa(test_tup):
    res = ""
    a, b = test_tup[60], test_tup[90]
    for i in range(a + 1, b):
        if i not in test_tup:
            res += str(i)
            break
    if len(res) % 2 == 1:
        return res
    else:
        return hex(int(res))
