
def return_binary_or_hexa(test_list):
    res = sum(x for x in range(test_list[33] + 1, test_list[78] - 1))
    if res % 2 == 0:
        return hex(res)
    else:
        return "0b" + bin(res)[2:]
