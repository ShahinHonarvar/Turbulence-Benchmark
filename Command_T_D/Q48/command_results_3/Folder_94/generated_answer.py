
import itertools

def return_binary_or_hexa(test_tup):
    res = 0
    for i in range(test_tup[42], test_tup[87], 2):
        if i not in test_tup:
            res += i
    return ("{:b}".format(res), "{:x}".format(res))
