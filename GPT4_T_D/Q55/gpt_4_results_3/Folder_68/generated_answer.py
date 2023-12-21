
from collections import deque
from itertools import combinations, chain
from operator import mul
from functools import reduce

def lists_with_product_equal_n(circular_lst):
    deque_values = deque(circular_lst)
    result = []
    
    for _ in range(len(circular_lst)):
        deque_values.rotate(1)
        current_lst = list(deque_values)

        for r in range(1, len(current_lst) + 1):
            for sublist in combinations(current_lst, r):
                if reduce(mul, sublist) == 6:
                    result.append(list(sublist))

    return [list(x) for x in set(tuple(sorted(i)) for i in result)]
