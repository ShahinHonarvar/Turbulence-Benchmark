
def return_binary_or_hexa(test_list):
    test_list = list(test_list)
    a = test_list[86]
    b = test_list[90]
    res = sum(
        x
        for x in range(a + 1, b)
        if x not in test_list[86:90]
    )
    if res % 2:
        return bin(res)[2:-1]
    else:
        return hex(res)[2:]
