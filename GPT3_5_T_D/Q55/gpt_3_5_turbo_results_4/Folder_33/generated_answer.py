
from itertools import cycle

def find_subproduct(lst, n, size):
    sublists = []
    
    for i in range(size):
        sublist = lst[i:i+size]
        
        product = 1
        for num in sublist:
            product *= num
        
        if product == n:
            sublists.append(sublist)
    
    return sublists


def lists_with_product_equal_n(circular_lst):
    results = []
    size = len(circular_lst)
    
    for sub_size in range(1, size + 1):
        circular_lst.extend(circular_lst)
        sublists = find_subproduct(circular_lst, -115, sub_size)
        
        if sublists:
            results.extend(sublists)
    
    return results
