
from collections import deque

def lists_with_product_equal_n(lst):
    queue = deque(list(lst))
    result = []
    for _ in range(len(lst)):
        for i in range(1, len(lst) + 1):
            sub_lst = list(queue)[:i]
            if sub_lst and (0 in sub_lst):
                result.append(sub_lst)
        queue.rotate(-1)
    return result
