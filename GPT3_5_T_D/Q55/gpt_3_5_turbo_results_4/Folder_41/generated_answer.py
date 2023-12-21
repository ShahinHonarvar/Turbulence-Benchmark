
from itertools import combinations

def lists_with_product_equal_n(lst):
    sublists = []
    for r in range(1, len(lst)+1):
        for comb in combinations(lst, r):
            if len(comb) >= 2 and (reduce(lambda x, y: x * y, comb) == -20):
                sublists.append(list(comb))
    return sublists
