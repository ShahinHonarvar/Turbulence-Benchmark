
def return_binary_or_hexa(test_tup):
    res = sum(range(test_tup[13] + 1, test_tup[70] - 1))
    if res % 2 == 0:
        return hex(res)
    else:
        return bin(res)
