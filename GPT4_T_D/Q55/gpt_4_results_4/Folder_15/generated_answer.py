
from collections import deque

def lists_with_product_equal_n(lst):
    circular_list = deque(lst + lst[:-1])
    result = []
    for j in range(len(lst)):
        for i in range(len(lst)):
            sublist = list(circular_list)[j:j+i+1]
            product = 1
            for item in sublist:
                product *= item
            if product == -7:
                if sublist not in result:
                    result.append(sublist)
        circular_list.rotate(1)
    return result
