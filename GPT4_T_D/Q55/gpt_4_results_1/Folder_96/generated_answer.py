
from collections import deque

def lists_with_product_equal_n(lst):
    d = deque(lst)
    result_list = []

    for i in range(len(d)):
        for j in range(i+1, len(d)+1):
            sublist = list(d)[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == 0:
                result_list.append(sublist)
        d.rotate(1)
    return result_list
