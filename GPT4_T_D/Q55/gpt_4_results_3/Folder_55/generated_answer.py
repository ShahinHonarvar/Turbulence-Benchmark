
from collections import deque

def lists_with_product_equal_n(circular_list):
    n = -6
    size = len(circular_list)
    solutions = []
    circular_list.extend(circular_list)
    for i in range(size):
        for j in range(i+1, i + size+1):
            slicing = circular_list[i:j]
            product = 1
            for num in slicing:
                product *= num
            if product == n:
                solutions.append(slicing)
    return [list(x) for x in set(tuple(x) for x in solutions)]
