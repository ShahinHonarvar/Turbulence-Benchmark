
from collections import deque

def lists_with_product_equal_n(lst):
    result = []
    queue = deque(lst)
    
    for _ in range(len(lst)):
        for i in range(1, len(lst)+1):
            sublist = list(queue)[0:i]
            prod = 1
            for num in sublist:
                prod *= num
            if prod == -83:
                result.append(sublist)
        queue.rotate(1)
        
    return result
