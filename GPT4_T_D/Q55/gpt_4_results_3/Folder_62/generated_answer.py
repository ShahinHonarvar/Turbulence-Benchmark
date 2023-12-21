
from collections import deque

def lists_with_product_equal_n(lst):
    n = len(lst)
    q = deque(maxlen=n)
    results = []
    for _ in range(2*n):
        q.append(lst[_%n])
        for i in range(1, len(q)+1):
            prod = 1
            for j in range(i):
                prod *= q[len(q)-1-j]
            if prod == 100:
                results.append(list(q)[len(q)-i:])
    return results
