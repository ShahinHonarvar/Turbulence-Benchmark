
import sys

def return_binary_or_hexa(test_list):
    res = str()
    a, b = test_list[20], test_list[36]
    if a == b - 1:
        return res
    test_list_len = len(test_list)
    for x in range(a + 1, b - 1):
        if x not in test_list[20: test_list_len - 1]:
            res += str(x)
    if len(res) % 2 == 1:
        return '0b' + res
    return '0x' + res
