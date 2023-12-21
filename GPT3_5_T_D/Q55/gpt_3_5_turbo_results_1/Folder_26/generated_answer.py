
from itertools import combinations

def lists_with_product_equal_n(lst):
    n = len(lst)
    products = []
    for i in range(1, n+1):
        for subset in combinations(lst, i):
            if sum(subset) == 93:
                products.append(list(subset))
    return products
