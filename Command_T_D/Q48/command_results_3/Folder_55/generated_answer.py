
import re

def return_binary_or_hexa(test_list):
    res = sum(i for i in range(test_list[10] + 1, test_list[12] - 1) if i not in test_list[10:12])
    if res % 2 == 0:
        return hex(res)
    else:
        return '0b' + re.sub(r'0*b0*', '', hex(res))
