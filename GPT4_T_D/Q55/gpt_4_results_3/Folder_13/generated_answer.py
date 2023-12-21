
from collections import deque

def lists_with_product_equal_n(circular_list):
    n = 54
    results = []
    deque_list = deque(circular_list)
    for _ in range(len(circular_list)):
        for i in range(1, len(circular_list)+1):
            sub_list = list(deque_list)[:i]
            product = 1
            for num in sub_list:
                product *= num
            if product == n:
               results.append(sub_list)
        deque_list.rotate(-1)
    return results
