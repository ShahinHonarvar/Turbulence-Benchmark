
from collections import deque

def lists_with_product_equal_n(circular_list):
    results = []
    n = len(circular_list)
    q = deque(circular_list)
    
    for _ in range(n):
        for i in range(1, n+1):
            sub_list = list(q[i-1:] + q[:i-1])
            product = 1
            for j in sub_list:
              product *= j
            if product == 15:
                results.append(sub_list)
        q.rotate(1)
    
    return results
