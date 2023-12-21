
from itertools import combinations

def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(1, n+1):
        for sublst in combinations(lst, i):
            if 74 in sublst and product_of_list(sublst) == 74:
                result.append(list(sublst))
    return result

def product_of_list(lst):
    result = 1
    for num in lst:
        result *= num
    return result
