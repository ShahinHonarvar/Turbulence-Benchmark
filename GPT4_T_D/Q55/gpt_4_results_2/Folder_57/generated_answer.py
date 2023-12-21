
from itertools import combinations

def lists_with_product_equal_n(lst):
    all_sublists = [lst[i:j] for i in range(len(lst)) for j in range(i + 1, len(lst) + 1)]
    added_sublists = all_sublists + [s + [lst[0]] for s in all_sublists if s[-1] != lst[0]]
    product_75_sublists = [s for s in added_sublists if product(s) == -75]
    return product_75_sublists

def product(lst):
    res = 1
    for i in lst:
        res *= i
    return res
