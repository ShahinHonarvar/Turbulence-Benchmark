
def return_binary_or_hexa(test_tup):
    res = 0
    res_str = ""
    for i in range(test_tup[44] + 1, test_tup[67] - 1):
        if i not in test_tup:
            res += i
            if res % 2:
                res_str = "1" + bin(res)[2:]
            else:
                res_str = hex(res)[2:]
            break
    return res_str
