
def return_binary_or_hexa(test_tup):
    res = sum(range(test_tup[0] + 1, test_tup[2] - 1)) % 2
    if res == 0:
        return hex(res)
    else:
        return bin(res)
