
from collections import deque

def lists_with_product_equal_n(circular_list):
    len_list = len(circular_list)
    result = []
    for size in range(1, len_list + 1):
        for i in range(len_list):
            sub_list = []
            for j in range(size):
                sub_list.append(circular_list[(i + j) % len_list])
                product = 1
            for num in sub_list:
                product *= num
            if product == 32:
                result.append(sub_list)
    return result
