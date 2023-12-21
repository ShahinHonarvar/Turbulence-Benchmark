
import re

def return_binary_or_hexa(test_list):
    res = test_list[68] + 1
    for i in range(test_list[69], test_list[97]):
        if test_list[i] == res:
            break
        res += 1
    return (res if res % 2 else '0x%x' % res)
