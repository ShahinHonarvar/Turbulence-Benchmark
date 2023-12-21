
from collections import deque
from itertools import combinations

def lists_with_product_equal_n(lst):
    circular_lst = deque(lst)
    result = []

    for _ in range(len(lst)):
        temp_list = list(circular_lst)
        for i in range(1, len(temp_list) + 1):
            for subset in combinations(temp_list, i):
                prod = 1
                for num in subset:
                    prod *= num
                if prod == 40:
                    result.append(list(subset))
        circular_lst.rotate(1)

    return result
