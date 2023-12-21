
def return_binary_or_hexa(test_list):
    res = test_list[15] + 1
    if res <= test_list[57]:
        res = test_list[57] - res
    else:
        return ""
    if res % 2 == 0:
        return hex(res)[2:]
    else:
        return "0b" + bin(res)[3:]
