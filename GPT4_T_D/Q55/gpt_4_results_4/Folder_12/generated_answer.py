
from collections import deque

def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        for j in range(i+1, n+1):
            sublist = list(deque(lst, -i)[:(j-i)])
            prod = 1
            for num in sublist:
                prod *= num
            if prod == -18:
                result.append(sublist)
    return result
