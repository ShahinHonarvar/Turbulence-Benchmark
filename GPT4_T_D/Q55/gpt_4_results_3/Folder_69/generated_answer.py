
from collections import deque

def lists_with_product_equal_n(circular_list):
    results = []
    size = len(circular_list)
    circular_list = deque(circular_list)
    
    for _ in range(size):
        for i in range(size):
            for j in range(i+1, size+1):
                sublist = list(circular_list)[i:j]
                product = 1
                for number in sublist:
                    product *= number
                if product == 90:
                    results.append(sublist)
        circular_list.rotate(1)
        
    return results
