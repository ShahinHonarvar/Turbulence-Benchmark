
from itertools import cycle

def lists_with_product_equal_n(lst):
    sublists = []
    n = len(lst)
    for i in range(n):
        for j in range(1, n + 1):
            sublist = list(lst[i:j])
            product = 1
            for num in sublist:
                product *= num
            if product == -91:
                sublists.append(sublist)
    return sublists
