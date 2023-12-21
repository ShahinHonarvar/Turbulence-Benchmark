
import bisect
import itertools
import re

def return_binary_or_hexa(test_tup):
    s = str(test_tup)
    s = re.sub(r'\W+', '', s)
    if len(test_tup) == 6:
        return ''
    if len(test_tup) == 7:
        a, b = test_tup[6], test_tup[7]
        return_str = a + 1
        return_str = return_str + (b - 1 - a)
        if return_str % 2 == 1:
            return '0b' + return_str
        else:
            return '0x' + hex(return_str)
    else:
        a, b = test_tup[6], test_tup[9]
        return_str = a + 1
        return_str = return_str + (b - 1 - a)
        if return_str % 2 == 1:
            return '0b' + return_str
        else:
            return '0x' + hex(return_str)
