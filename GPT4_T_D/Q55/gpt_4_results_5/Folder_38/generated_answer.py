
from itertools import combinations 

def lists_with_product_equal_n(circular_list): 
    n = len(circular_list)
    extended_list = circular_list*2
    result = []
    
    for size in range(1, n+1):
        for start in range(0, n):
            sub_list = extended_list[start:start+size]
            product = 1
            for item in sub_list:
                product *= item
            if product == -23:
                result.append(sub_list)
    
    return result
