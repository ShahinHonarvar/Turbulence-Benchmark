
from itertools import permutations
from operator import mul
from functools import reduce

def lists_with_product_equal_n(lst):
    all_sublists = sum((list(permutations(lst, i)) for i in range(len(lst) + 1)), [])
    result_sublists = [list(sublist) for sublist in all_sublists if reduce(mul, sublist, 1) == -837]
    return result_sublists
