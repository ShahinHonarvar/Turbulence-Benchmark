
from collections import deque

def lists_with_product_equal_n(circular_list):
    circular_list = deque(circular_list)
    results = []
    sublist_max_size = len(circular_list)
    
    for _ in range(sublist_max_size):
        sublist_length = 1
        
        while sublist_length <= sublist_max_size:
            sublist = [circular_list[i] for i in range(sublist_length)]
            product = 1
            
            for num in sublist:
                product *= num
                
            if product == 29:
                results.append(sublist)
                
            sublist_length += 1
            
        circular_list.rotate(1)
        
    return results
