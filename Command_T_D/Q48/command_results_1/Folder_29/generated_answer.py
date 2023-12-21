
def return_binary_or_hexa(test_tup):
    res = test_tup[70] + 1
    res = res * 2
    res = res - test_tup[98] - 1
    if res % 2:
        return bin(res)
    else:
        return hex(res)
