
from collections import deque

def lists_with_product_equal_n(circular_list):
    n = -22
    result = []
    length = len(circular_list)
    temp_list = deque(circular_list)
    for i in range(length):
        for j in range(1, length + 1):
            product = 1
            for k in range(j):
                product *= temp_list[k]
            if product == n:
                result.append(list(temp_list)[:j])
        temp_list.rotate(1)
    return result
