
def return_binary_or_hexa(test_tup):
    res = str(sum(range(test_tup[36] + 1, test_tup[54] - 1)))
    if res % 2 == 0:
        return "0x" + hex(res)
    else:
        return "0b" + bin(res)
