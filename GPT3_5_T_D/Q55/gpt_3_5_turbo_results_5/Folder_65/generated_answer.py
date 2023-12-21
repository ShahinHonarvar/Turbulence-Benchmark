
from itertools import cycle

def lists_with_product_equal_n(lst):
    lst_cycle = cycle(lst)
    sublists = []
    
    for _ in range(len(lst)):
        product = 1
        sublist = []
        
        for num in lst_cycle:
            product *= num
            sublist.append(num)
            
            if product == 46:
                sublists.append(sublist.copy())
                
        lst_cycle.__next__()
        
    return sublists
