
import re

def return_binary_or_hexa(test_tup):
    res = str(sum(range(test_tup[10]+1, test_tup[97]-1)))
    if res%2:
        res = re.sub(r'0x', '', res)
        res = re.sub(r'0b', '', res)
        res = re.sub(r'0p', '', res)
        res = re.sub(r'0d', '', res)
        res = re.sub(r'0o', '', res)
    else:
        res = re.sub(r'0x', '', res)
    return res
