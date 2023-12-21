
from collections import deque

def lists_with_product_equal_n(circular_list):
    result = []
    list_len = len(circular_list)
    circular_list = deque(circular_list)

    for _ in range(list_len):
        for i in range(1, list_len+1):
            sub_list = list(circular_list)[:i]

            product = 1
            for num in sub_list:
                product *= num

            if product == 247:
                result.append(sub_list)
            
        circular_list.rotate(-1)
    return result
