
from itertools import combinations

def lists_with_product_equal_n(circular_lst):
    result = []
    
    for i in range(1, len(circular_lst) + 1):
        for combo in combinations(circular_lst, i):
            product = 1
            for num in combo:
                product *= num
            if product == 247:
                result.append(list(combo))
    
    return result
