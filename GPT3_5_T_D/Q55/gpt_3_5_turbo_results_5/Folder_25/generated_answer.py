
from itertools import combinations

def lists_with_product_equal_n(lst):
    sublists = []
    
    for i in range(1, len(lst) + 1):
        for comb in combinations(lst, i):
            product = 1
            for num in comb:
                product *= num
            if product == -32:
                sublists.append(list(comb))
                
    return sublists
