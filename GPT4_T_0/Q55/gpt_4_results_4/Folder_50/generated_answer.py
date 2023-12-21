
from collections import deque

def lists_with_product_equal_n(circular_list):
    n = 45
    result = []
    for i in range(len(circular_list)):
        for j in range(i, len(circular_list)):
            sublist = circular_list[i:j+1]
            product = 1
            for num in sublist:
                product *= num
            if product == n:
                result.append(sublist)
        circular_list.rotate(-1)
    return result
