
from numpy import prod
from collections import deque

def lists_with_product_equal_n(lst):
    equal_product_sublists = []
    size = len(lst)
    
    for sublist_len in range(1, size + 1):
        circular_lst = deque(lst)
        iter_cycle = 0
        while iter_cycle < size:
            sublist = [circular_lst[j] for j in range(sublist_len)]
            if prod(sublist) == 91:
                equal_product_sublists.append(sublist)
            circular_lst.rotate(-1)
            iter_cycle += 1
            
    return equal_product_sublists
