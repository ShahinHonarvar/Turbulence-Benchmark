
from collections import deque

def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for i in range(n):
        queue = deque()
        product = 1
        for j in range(i, i+n):
            queue.append(lst[j%n])
            product *= lst[j%n]
            while product > 15 and queue:
                removed = queue.popleft()
                product /= removed
            if product == 15:
                result.append(list(queue))
    return result
