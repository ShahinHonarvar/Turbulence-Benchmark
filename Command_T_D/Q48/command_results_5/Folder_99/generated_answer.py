
import re

def return_binary_or_hexa(test_tup):
    res = sum(range(test_tup[0] + 1, test_tup[1] - 1))
    return hex(res) if res <= 0xff and res % 2 == 0 else '0b' + re.sub(r'0+$', '', bin(res))
