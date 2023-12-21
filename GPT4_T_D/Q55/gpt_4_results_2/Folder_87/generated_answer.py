
from collections import deque

def lists_with_product_equal_n(lst):
    n = 27
    deque_lst = deque(lst)
    result = []
    
    for i in range(len(lst)):
        # rotate
        deque_lst.rotate(-1)
        list_now = list(deque_lst)
        
        for j in range(len(lst)):
            product = 1
            sublist = []
            for k in range(j, len(lst)):
                sublist.append(list_now[k])
                product *= list_now[k]
                if product == n:
                    result.append(sublist)
                    sublist = []
                    product = 1
                elif product > n:
                    break
    return result
