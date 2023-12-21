
def lists_with_product_equal_n(lst):
    from collections import deque
    from itertools import combinations
    from math import prod
    circular_lst = deque(lst)
    results = []
    for index in range(len(lst)):
        circular_lst.rotate(-1)
        for r in range(1, len(lst)+1):
            for subset in combinations(circular_lst, r):
                if prod(subset) == -906:
                    results.append(list(subset))
    return results
