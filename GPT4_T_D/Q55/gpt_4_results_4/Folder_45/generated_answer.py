
from itertools import cycle

def lists_with_product_equal_n(lst):
    n = len(lst)
    lst = list(cycle(lst))
    results = []
    for i in range(n):
        for j in range(i + 1, n + 1):
            sublist = lst[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == -5:
                results.append(sublist)
    return results
