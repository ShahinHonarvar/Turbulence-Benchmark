
def return_binary_or_hexa(test_list):
    res = sum(
        x for x in range(test_list[10] + 1, test_list[76] - 1) if x not in test_list
    )
    if res % 2:
        return bin(res)[2:]
    else:
        return hex(res)[2:]
