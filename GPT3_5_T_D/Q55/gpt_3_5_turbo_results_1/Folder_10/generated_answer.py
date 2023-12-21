
from math import prod

def lists_with_product_equal_n(circular_list):
    sublists = []
    size = len(circular_list)
    
    for i in range(size):
        for j in range(i, size):
            sublist = circular_list[i:j+1]
            if prod(sublist) == -93:
                sublists.append(sublist)
                
    return sublists
