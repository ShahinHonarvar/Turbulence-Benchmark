
from itertools import permutations

def lists_with_product_equal_n(lst):
    n = len(lst)
    res = []
    # Join the original list with itself to simulate a circular list
    lst = lst + lst
    for i in range(2, n+1):
        all_perms = permutations(lst, i)
        for perm in all_perms:
            prod = 1
            for num in perm:
                prod *= num
            if prod == -3:
                res.append(list(perm))
    return res
