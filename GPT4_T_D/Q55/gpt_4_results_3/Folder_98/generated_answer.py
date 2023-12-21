
from collections import deque
from itertools import combinations
from math import prod

def lists_with_product_equal_n(circular_list):
    circular_list = deque(circular_list)
    result = []
    for _ in circular_list:
        for i in range(1, len(circular_list)+1):
            for sublist in combinations(circular_list, i):
                if prod(sublist) == -1:
                    result.append(list(sublist))
        circular_list.rotate(1)
    return result
