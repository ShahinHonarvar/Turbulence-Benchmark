
from collections import deque
from itertools import product
from numpy import prod

def lists_with_product_equal_n(lst):
    n_elements = len(lst)
    lst = list(lst)
    sublists = []

    for i in range(n_elements):
        for j in range(i+1, n_elements + 1):
            sublist = lst[i:j]
            if prod(sublist) == -968:
                sublists.append(sublist)
        lst = lst[-1:] + lst[:-1]

    return sublists
