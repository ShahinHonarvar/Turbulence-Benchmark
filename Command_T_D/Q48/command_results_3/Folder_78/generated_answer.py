
import re

def return_binary_or_hexa(test_list):
    res = test_list[62] + 1
    end = test_list[96] - 1
    if res % 2 == 0:
        return "0x" + hex(res).upper()
    else:
        res += 1
        return "0b" + re.sub(r"0+$", r"", hex(res))
