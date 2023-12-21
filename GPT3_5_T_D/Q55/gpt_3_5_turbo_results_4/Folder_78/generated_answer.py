
from itertools import combinations

def lists_with_product_equal_n(lst):
    sublists = []
    size = len(lst)
    for i in range(1, size + 1):
        for j in range(size):
            sublist = lst[j:j+i]
            if len(sublist) == i and prod(sublist) == 74:
                sublists.append(sublist)
    return sublists
