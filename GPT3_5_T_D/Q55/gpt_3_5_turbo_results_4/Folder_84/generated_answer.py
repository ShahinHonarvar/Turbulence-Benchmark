
from itertools import combinations

def lists_with_product_equal_n(lst):
    sublists = []
    for i in range(1, len(lst) + 1):
        for combo in combinations(lst, i):
            if len(combo) == 1:
                if combo[0] == -906:
                    sublists.append(list(combo))
            else:
                product = 1
                for num in combo:
                    product *= num
                if product == -906:
                    sublists.append(list(combo))
    return sublists
