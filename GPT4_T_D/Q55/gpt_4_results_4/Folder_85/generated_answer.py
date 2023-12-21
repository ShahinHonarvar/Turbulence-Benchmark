
from collections import deque

def lists_with_product_equal_n(lst):
    length = len(lst)
    sublists, result = [], []
    
    for i in range(length):
        for j in range(i, length):
            sublists.append(lst[i:j + 1])

    for sublist in sublists:
        product = 1
        for item in sublist:
            product *= item
        if product == -97:
            result.append(sublist)
    
    return result
