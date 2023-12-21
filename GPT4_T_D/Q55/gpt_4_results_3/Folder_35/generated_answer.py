
from collections import deque

def lists_with_product_equal_n(num_list):
    n = len(num_list)
    circular_num_list = deque(num_list)
    result = []
    
    for _ in range(n):
        for i in range(n):
            for j in range(i+1, n+1):
                sublist = list(circular_num_list)[i:j]
                product = 1
                for num in sublist:
                    product *= num
                if product == 83:
                    result.append(sublist)
        circular_num_list.rotate(1)
    return result
