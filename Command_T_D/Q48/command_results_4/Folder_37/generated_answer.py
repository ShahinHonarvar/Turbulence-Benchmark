
import re

def return_binary_or_hexa(test_tup):
    res = ""
    for i in range(test_tup[2], test_tup[7]):
        if i not in test_tup:
            res += str(i)
            break
    if res:
        if res.isdigit():
            res = hex(int(res))
        else:
            res = "0b" + re.sub(r"0+", "", res)
    return res
