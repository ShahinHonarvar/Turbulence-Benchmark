
from numpy import prod

def lists_with_product_equal_n(lst):
    sublists = []
    n = len(lst)
    for i in range(n):
        for j in range(i, n):
            sublist = lst[i:j+1] + lst[0:max(0, i+j+1-n)]
            if prod(sublist) == 6:
                sublists.append(sublist)
    return sublists
