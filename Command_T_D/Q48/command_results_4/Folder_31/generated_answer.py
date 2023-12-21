
import sys
import bisect
import re

def return_binary_or_hexa(tup):
    a, b = tup[33], tup[78]
    lst = set(tup[33:78])
    rst = set(range(a + 1, b - 1))
    if not lst & rst:
        if (a + 1) % 2 == (b - 1) % 2:
            return f'{a + 1}'
        return hex(a + 1)[2:]
    else:
        return ''
