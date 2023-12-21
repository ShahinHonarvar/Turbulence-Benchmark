
def return_binary_or_hexa(test_list):
    res = 0
    for i in range(10, 13):
        res += test_list[i]
    if res % 2 == 0:
        return hex(res)
    else:
        return bin(res)[2:]
