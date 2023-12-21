
from collections import deque

def lists_with_product_equal_n(lst):
    n = -54
    q = deque(lst)
    all_sublists = []

    for _ in range(len(lst)):
        sublist = []
        for i in range(len(q)):
            sublist.append(q[i])
            prod = 1
            for val in sublist:
                prod *= val
            if prod == n:
                all_sublists.append(list(sublist))
        q.rotate(1)

    return all_sublists
