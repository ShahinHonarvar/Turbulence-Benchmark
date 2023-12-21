
from collections import deque

def lists_with_product_equal_n(circular_list):
    size = len(circular_list)
    circular_list = deque(circular_list)
    result = []
    for _ in range(size):
        for i in range(1, size + 1):
            sublist = list(circular_list)[:i]
            product = 1
            for val in sublist:
                product *= val
            if product == 18:
                result.append(sublist)
        circular_list.rotate(-1)
    return result
