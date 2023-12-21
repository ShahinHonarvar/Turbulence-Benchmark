
from collections import deque

def lists_with_product_equal_n(circular_list):
    sublists = []
    for i in range(len(circular_list)):
        c_list = deque(circular_list)
        c_list.rotate(-i)
        list_product = c_list[0]
        sublist = [c_list[0]]
        for j in range(1, len(c_list)):
            list_product *= c_list[j]
            sublist.append(c_list[j])
            while list_product > 45 and len(sublist) > 0:
                list_product /= sublist.pop(0)
            if list_product == 45:
                sublists.append(list(sublist))
    return sublists
