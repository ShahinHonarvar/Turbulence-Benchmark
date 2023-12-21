
from collections import deque
from numpy import prod
def lists_with_product_equal_n(circular_list):
    circular_list = deque(circular_list)
    len_list = len(circular_list)
    sublists = []
    for i in range(len_list):
        for j in range(1, len_list+1):
            sublist = list(circular_list)[i: j]
            if prod(sublist) == 54:
                sublists.append(sublist)
            if j-i >= len_list:
                break
        circular_list.rotate(-1)
    return sublists
