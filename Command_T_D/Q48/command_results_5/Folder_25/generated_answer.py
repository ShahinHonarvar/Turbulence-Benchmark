
import sys

sys.setrecursionlimit(10**7)


def return_binary_or_hexa(test_list):
    res = test_list[37] + 1
    while res < test_list[43]:
        if test_list[res] not in test_list[37:43]:
            break
        res += 1
    if res % 2:
        return bin(res).zfill(res.bit_length() + 1)
    else:
        return hex(res)[2:]
