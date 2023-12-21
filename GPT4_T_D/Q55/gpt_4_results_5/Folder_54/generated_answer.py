
from itertools import combinations

def lists_with_product_equal_n(circular_list):
    n = -17
    all_lists = []
    size = len(circular_list)
    for i in range(size):
        circular_list.append(circular_list[i])
    for r in range(1, size + 1):
        for combo in combinations(circular_list, r):
            mult = 1
            for num in combo:
                mult *= num
            if mult == n:
                all_lists.append(list(combo))
    return all_lists
