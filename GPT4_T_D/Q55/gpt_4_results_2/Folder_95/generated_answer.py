
from collections import deque

def lists_with_product_equal_n(lst):
    res = []
    length = len(lst)
    lst += lst
    for n in range(2, length+1):
        for i in range(length):
            sublist = lst[i:i+n]
            product = 1
            for item in sublist:
                product *= item
            if product == 28:
                res.append(sublist)
    return [list(i) for i in set(tuple(i) for i in res)]
