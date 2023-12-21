
from collections import deque

def lists_with_product_equal_n(lst):
    n = len(lst)
    lst = deque(lst)
    result = []
    for _ in range(n):
        for i in range(1, n+1):
            sublist = list(lst)[:i]
            product = 1
            for num in sublist:
                product *= num
            if product == -57:
                result.append(sublist)
        lst.rotate(1)
    return result
