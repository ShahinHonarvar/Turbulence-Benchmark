
from collections import deque

def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    circular_list = deque(circular_list)
    result = []

    for i in range(n):
        for j in range(1, n + 1):
            sublist = list(circular_list)[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == -81:
                result.append(sublist)
        circular_list.rotate(1)
    
    return result
