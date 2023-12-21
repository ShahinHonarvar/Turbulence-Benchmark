
from collections import deque

def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    circular_list = list(deque(circular_list, n))
    results = []
    
    if n <= 0: return results

    for i in range(n):
        for j in range(i+1, n+1):
            sublist = circular_list[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == 90:
                results.append(sublist)
                
    return results
