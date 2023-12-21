
from collections import deque

def lists_with_product_equal_n(lst):
    sublists = []
    deque_list = deque(lst)
    len_lst = len(lst)
    for shift in range(len_lst):
        deque_list.rotate(1)
        for i in range(len_lst):
            for j in range(i + 1, len_lst + 1):
                sublist = list(deque_list)[i:j]
                prod = 1
                for elem in sublist:
                    prod *= elem
                if prod == 47:
                    sublists.append(sublist)
    return sublists
