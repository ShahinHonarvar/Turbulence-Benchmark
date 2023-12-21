
def return_binary_or_hexa(test_list):
    res = test_list[3] + 1
    res = res + test_list[9] - test_list[3] - 1
    if res % 2 == 0:
        return hex(res)
    else:
        return bin(res)
