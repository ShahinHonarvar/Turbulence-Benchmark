
def return_binary_or_hexa(test_list):
    res = 0
    a, b = sorted(test_list)[20], sorted(test_list)[51]
    for i in range(a + 1, b - 1):
        if i not in test_list:
            res += i
    if res % 2:
        return bin(res).rstrip("0b")
    else:
        return hex(res).rstrip("0x")
