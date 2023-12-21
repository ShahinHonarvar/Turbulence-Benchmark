
def return_binary_or_hexa(test_list):
    res = 0
    a = test_list[200]
    b = test_list[202]
    for i in range(a + 1, b - 1):
        if i not in test_list[200:202]:
            res += i
    if res % 2 == 1:
        return bin(res)[2:]
    else:
        return hex(res)[2:]
