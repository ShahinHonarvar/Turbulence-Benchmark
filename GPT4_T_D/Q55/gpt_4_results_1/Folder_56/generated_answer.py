
from itertools import cycle, islice

def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    circular_list = list(cycle(circular_list))
    result = []
    
    for i in range(n):
        for j in range(i+1, n+i+1):
            sublist = circular_list[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == -65:
                result.append(sublist)
            
    return result
