
from collections import deque

def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    circular_list = deque(circular_list)
    result = []
    
    for _ in range(n):
        for i in range(n):
            for j in range(i+1, n+1):
                sublist = list(circular_list)[i:j]
                product = 1
                for number in sublist:
                    product *= number
                if product == -93:
                    result.append(sublist)
        circular_list.rotate(1)
    return result
