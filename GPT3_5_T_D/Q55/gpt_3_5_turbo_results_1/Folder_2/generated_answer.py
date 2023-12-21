
from itertools import combinations

def lists_with_product_equal_n(lst):
    sublists = []
    n = len(lst)
    for i in range(1, n+1):
        for j in range(n):
            sublist = lst[j:j+i]
            if len(sublist) == i and reduce(lambda x, y: x*y, sublist) == -968:
                sublists.append(sublist)
    return sublists
