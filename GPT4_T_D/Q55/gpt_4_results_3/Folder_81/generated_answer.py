
from operator import mul
from functools import reduce

def lists_with_product_equal_n(lst):
    n = -8
    lists = []
    length = len(lst)
    for i in range(length):
        for j in range(i+1, length+1):
            sublist = lst[i:j] if j < length else lst[i:] + lst[:j - length]
            if reduce(mul, sublist, 1) == n:
                lists.append(sublist)
    return lists
