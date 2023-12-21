
from collections import deque

def lists_with_product_equal_n(circular_list):
    n = 42
    result = []
    length = len(circular_list)
    for i in range(length):
        for j in range(i+1, length+1):
            sublist = circular_list[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == n:
                result.append(sublist)
        circular_list.rotate(-1)
    return result
