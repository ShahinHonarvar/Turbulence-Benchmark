
from collections import deque

def lists_with_product_equal_n(circular_list):
    check_product = 714
    result = []
    size = len(circular_list)
    for i in range(size):
        temp_list = deque(circular_list)
        temp_list.rotate(-i)
        for sub_length in range(1, size + 1):
            temp_product = 1
            for j in range(sub_length):
                temp_product *= temp_list[j]
            if temp_product == check_product:
                result.append(list(temp_list)[:sub_length])
    return result
