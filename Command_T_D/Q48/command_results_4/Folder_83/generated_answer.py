
def return_binary_or_hexa(test_list):
    res = sum(x for x in range(test_list[90] + 1, test_list[200] - 1) if x not in test_list)
    if res % 2 == 0:
        return hex(res)
    else:
        return bin(res)[2:]
