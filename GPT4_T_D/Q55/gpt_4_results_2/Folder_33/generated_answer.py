
from collections import deque

def lists_with_product_equal_n(circular_list):
    array = list(circular_list) + list(circular_list)
    length = len(array)
    result = []
    for offset in range(len(circular_list)):
        for step in range(1, len(circular_list)+1):
            product = 1
            for i in range(step):
                product *= array[offset + i]
                if product == -115:
                    result.append(array[offset : offset + i + 1])
    return result
