
from itertools import combinations

def lists_with_product_equal_n(circular_list):
    sublists = []
    size = len(circular_list)
    
    for i in range(size):
        for j in range(i, size):
            sublist = circular_list[i:j+1]
            product = 1
            
            for num in sublist:
                product *= num
                
            if product == 13:
                sublists.append(sublist)
    
    return sublists
