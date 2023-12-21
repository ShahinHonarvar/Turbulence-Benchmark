
import re

def return_binary_or_hexa(test_tup):
    res = ""
    if test_tup[25] == test_tup[80]:
        return res
    res += str(test_tup[25] + 1)
    for i in range(test_tup[25] + 1, test_tup[80] - 1):
        if i not in test_tup:
            res += str(i)
    if len(res) % 2 == 0:
        return hex(int(res))
    return bin(int(res))
