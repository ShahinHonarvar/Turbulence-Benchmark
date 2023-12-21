
import re

def return_binary_or_hexa(test_tup):
    res = test_tup[a+1:b-1]
    if not res:
        return ""
    if len(res)%2:
        return "0b" + bin(sum(res))[2:-1]
    return "0x" + re.sub(r"0+(0|1)0+", r"0\1", hex(sum(res))[2:])
