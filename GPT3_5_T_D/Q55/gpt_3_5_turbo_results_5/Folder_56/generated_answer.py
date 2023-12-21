
from itertools import chain, combinations

def lists_with_product_equal_n(lst):
    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result

    def find_sublists(lst):
        sublists = []
        for i in range(1, len(lst) + 1):
            for combination in combinations(lst, i):
                sublists.append(list(combination))
        return sublists

    n = -65
    sublists = find_sublists(list(chain(lst, lst[:-1])))
    return [sublist for sublist in sublists if product(sublist) == n]
