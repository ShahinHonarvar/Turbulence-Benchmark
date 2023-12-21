
import itertools

def return_binary_or_hexa(test_tup):
    a, b = test_tup[51], test_tup[76]
    res = sum(i for i in range(a + 1, b - 1) if i not in test_tup)
    if res % 2 == 0:
        return hex(res)[2:]
    else:
        return bin(res)[2:]
