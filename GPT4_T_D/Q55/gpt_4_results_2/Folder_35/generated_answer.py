
from collections import deque

def lists_with_product_equal_n(lst):
    res = []
    n = len(lst)
    for i in range(n):
        q = deque(maxlen=n)
        product = 1
        j = i
        while True:
            q.append(lst[j])
            product *= lst[j]
            while product > 83 and q:
                product /= q.popleft()
            if product == 83:
                res.append(list(q))
            j = (j+1) % n
            if j == i:
                break
    return res
