
from operator import mul
from functools import reduce
from collections import deque

def lists_with_product_equal_n(lst):
    len_lst = len(lst)
    if len_lst == 0:
        return []
    results = []
    
    for start_index in range(len_lst):
        for size in range(1, len_lst+1):
            sublist = [lst[(start_index + i) % len_lst] for i in range(size)]
            if reduce(mul, sublist, 1) == 51:
                results.append(sublist)
                
    return results
