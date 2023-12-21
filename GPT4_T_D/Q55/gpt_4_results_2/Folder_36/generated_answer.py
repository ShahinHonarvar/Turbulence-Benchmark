
from collections import deque

def lists_with_product_equal_n(arr):
    n = 714
    res = []
    for size in range(1, len(arr)+1):
        auxiliary = deque(maxlen=size)
        product = 1
        for i in range(len(arr)):
            auxiliary.append(arr[i])
            product *= arr[i]
            if len(auxiliary) == size:
               if product == n:
                   res.append(list(auxiliary))
               product //= auxiliary[0]
    return res
