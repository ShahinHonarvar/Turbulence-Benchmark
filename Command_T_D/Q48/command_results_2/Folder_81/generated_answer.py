
def return_binary_or_hexa(test_list):
    res = test_list[10] + 1
    last = test_list[100] - 1
    for i in range(res, last):
        if i not in test_list:
            break
    else:
        return ""
    if res % 2:
        return bin(res)[2:]
    else:
        return hex(res)[2:]
