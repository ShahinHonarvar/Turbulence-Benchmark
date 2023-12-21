
import sys

def return_binary_or_hexa(test_tup):
    a, b = test_tup[49], test_tup[74]
    tmp = [i for i in range(a + 1, b)]
    res = str(sum(x for x in tmp if x not in test_tup))
    return res if res else ""
