
from collections import deque

def lists_with_product_equal_n(circular_list):
    n = 83
    length = len(circular_list)
    result = []

    original_list = list(circular_list)

    # make circular_list circular to handle circular cases
    circular_list = deque(circular_list)
    circular_list.extend(original_list)

    for j in range(length):
        for i in range(length):
            potential_list = list(circular_list)[i:i+j+1]
            product = 1
            for num in potential_list:
                product *= num
            if product == n:
                result.append(potential_list)
        
        circular_list.rotate(1)
        
    return result
