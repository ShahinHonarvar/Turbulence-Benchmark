
from collections import deque

def lists_with_product_equal_n(circular_list):
    size = len(circular_list)
    res = []
    for _ in range(size):
        for j in range(1, size + 1):
            sublist = circular_list[0:j]
            product = 1
            for num in sublist:
                product *= num
            if product == -690:
                res.append(sublist)
        circular_list.rotate(-1)
    return res
