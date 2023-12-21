
from collections import deque

def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    circ_list = circular_list + circular_list
    result = []
    for idx in range(n):
        for sub_idx in range(idx+1, idx+n+1):
            sublist = circ_list[idx:sub_idx]
            product = 1
            for number in sublist:
                product *= number
            if product == 42:
                result.append(sublist)
    return result
