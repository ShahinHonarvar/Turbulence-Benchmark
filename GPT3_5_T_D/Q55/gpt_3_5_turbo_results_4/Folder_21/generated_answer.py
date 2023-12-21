
from itertools import combinations

def lists_with_product_equal_n(circular_list):
    sublists = []
    size = len(circular_list)
    
    for l in range(1, size+1):
        for sublist in combinations(circular_list, l):
            if reduce((lambda x, y: x * y), sublist) == 851:
                sublists.append(list(sublist))
    
    return sublists
