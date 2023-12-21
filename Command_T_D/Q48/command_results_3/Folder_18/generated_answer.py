
def return_binary_or_hexa(test_list):
    a = test_list[56]
    b = test_list[90]
    res = sum(x for x in range(a + 1, b))
    if res % 2 == 1:
        return bin(res)[2:]
    else:
        return hex(res)[2:]
