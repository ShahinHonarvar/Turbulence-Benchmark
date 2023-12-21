
from collections import deque

def lists_with_product_equal_n(circular_list):
    n = 45
    result = []
    for i in range(len(circular_list)):
        product = 1
        sublist = []
        for j in range(i, len(circular_list) + i):
            index = j % len(circular_list)
            product *= circular_list[index]
            sublist.append(circular_list[index])
            if product == n:
                result.append(sublist.copy())
            if product > n:
                break
    return result
