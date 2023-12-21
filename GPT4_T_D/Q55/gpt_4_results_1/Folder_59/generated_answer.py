
from collections import deque

def lists_with_product_equal_n(lst):
    sublists_n = []
    for start_index, start_value in enumerate(lst):
        temp_list = deque(lst)
        temp_list.rotate(-start_index)
        product = 1
        sublist = []
        for i in temp_list:
            product *= i
            sublist.append(i)
            if product == -3:
                sublists_n.append(list(sublist))
            elif product % -3 != 0:
                product = 1
                sublist = []
    return sublists_n
