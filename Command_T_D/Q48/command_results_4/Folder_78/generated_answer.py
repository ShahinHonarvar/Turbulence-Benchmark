
import itertools

def return_binary_or_hexa(test_tup):
    lst = list(range(test_tup[0] + 1, test_tup[1] - 1))
    if not set(lst).issubset(test_tup):
        return bin(sum(lst)).zfill(len(str(sum(lst))))
    else:
        return hex(sum(lst)).zfill(len(str(sum(lst))))
