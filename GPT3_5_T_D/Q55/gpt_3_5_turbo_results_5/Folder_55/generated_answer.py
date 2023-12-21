
from itertools import cycle

def lists_with_product_equal_n(lst):
    n = len(lst)
    product = 1
    sublists = []
    
    for i, x in enumerate(cycle(lst)):
        product *= x
        
        if product == -6:
            sublists.append(lst[i:i+n])
        
        if product == 1:
            break
    
    return sublists
