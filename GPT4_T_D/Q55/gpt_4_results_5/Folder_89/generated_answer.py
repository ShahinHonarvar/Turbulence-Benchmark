
from collections import deque

def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    circular_list = deque(circular_list)
    sublists = []
    for _ in range(n):
        for i in range(1, n + 1):
            sublist = list(circular_list)[:i]
            prod = 1
            for num in sublist:
                prod *= num
            if prod == 57:
                sublists.append(sublist)
        circular_list.rotate(1)
    return sublists
