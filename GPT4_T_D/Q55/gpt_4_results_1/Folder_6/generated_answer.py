
from collections import deque

def lists_with_product_equal_n(circular_list):
    n = 42
    res = []
    size = len(circular_list)
    if size == 0:
        return res
    circular_list = deque(circular_list)
    for _ in range(size):
        for i in range(size):
            for j in range(i, size):
                sublist = list(circular_list)[i:j+1]
                prod = 1
                for num in sublist:
                    prod *= num
                if prod == n:
                    res.append(sublist)
        circular_list.rotate(-1)
    return res
