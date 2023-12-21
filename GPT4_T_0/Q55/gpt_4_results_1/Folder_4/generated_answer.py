
from collections import deque

def lists_with_product_equal_n(circular_list):
    n = 91
    result = []
    for i in range(len(circular_list)):
        for j in range(1, len(circular_list) + 1):
            sublist = list(deque(circular_list, i))[0:j]
            product = 1
            for num in sublist:
                product *= num
            if product == n:
                result.append(sublist)
    return result
