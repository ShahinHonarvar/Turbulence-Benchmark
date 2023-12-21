
from collections import deque

def lists_with_product_equal_n(lst):
    n = 851
    result = []
    size = len(lst)

    for i in range(size):
        temp_list = deque(lst[i:] + lst[:i], maxlen=size)
        for j in range(1, size+1):
            product = 1
            for k in range(j):
                product *= temp_list[k]
            if product == n:
                result.append(list(temp_list)[:j])
    return result
