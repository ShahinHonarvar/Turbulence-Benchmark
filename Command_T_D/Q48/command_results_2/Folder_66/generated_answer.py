
def return_binary_or_hexa(test_list):
    res = 0
    for i in range(len(test_list) - 1):
        res += test_list[i + 1] - test_list[i] - 1
    if res % 2 == 0:
        return hex(res)
    else:
        return '0b' + bin(res)[2:]
