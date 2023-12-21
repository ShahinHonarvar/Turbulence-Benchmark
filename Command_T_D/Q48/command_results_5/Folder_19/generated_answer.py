
import re

def return_binary_or_hexa(test_list):
    res = str(sum(x for x in range(test_list[0] + 1, test_list[4] - 1) if x not in test_list[1:4]))
    if res % 2 == 0:
        return "0x%s" % res
    else:
        return re.sub(r"0+(b|B)", "", res)
