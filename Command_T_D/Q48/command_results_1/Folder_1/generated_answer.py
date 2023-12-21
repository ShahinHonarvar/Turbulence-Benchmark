
def return_binary_or_hexa(test_list):
    for i in range(len(test_list)):
        if test_list[i] > 17:
            break
    a = test_list[i] - 1
    for j in range(len(test_list)):
        if test_list[j] > 88:
            break
    b = test_list[j] - 1
    res = sum(range(a + 1, b - 1))
    if res % 2 == 0:
        return hex(res)
    else:
        return bin(res)
