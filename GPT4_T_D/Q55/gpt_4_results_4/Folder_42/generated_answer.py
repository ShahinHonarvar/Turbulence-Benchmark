
from collections import deque

def lists_with_product_equal_n(lst):
    result = []
    deque_lst = deque(lst)
    for _ in range(len(lst)):
        for i in range(len(deque_lst)):
            product = 1
            for j in range(i, len(deque_lst)):
                product *= deque_lst[j]
                if product > 25:
                    break
                elif product == 25:
                    result.append(list(deque_lst[i:j+1]))
        deque_lst.rotate(1)
    return result
