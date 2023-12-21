
from itertools import combinations

def lists_with_product_equal_n(lst):
    result = []
    size = len(lst)
    for sub_size in range(1, size + 1):
        for i in range(size):
            sublist = lst[i:i+sub_size]
            if sublist and is_sublist_product_negative(sublist):
                result.append(sublist)
    return result

def is_sublist_product_negative(sublist):
    return any(product == -81 for product in product_combinations(sublist))

def product_combinations(sublist):
    return [prod(pair) for pair in combinations(sublist, 2)]

def prod(pair):
    return pair[0] * pair[1]
