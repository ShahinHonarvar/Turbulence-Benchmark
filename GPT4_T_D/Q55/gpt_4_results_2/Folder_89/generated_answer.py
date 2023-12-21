
from collections import deque

def lists_with_product_equal_n(lst):
    circular_lst = deque(lst)
    sublists = []
    for i in range(len(lst)):
        circular_lst.rotate(1)
        for j in range(len(circular_lst)):
            for k in range(1, len(circular_lst) + 1 - j):
                sublist = list(circular_lst)[j:j+k]
                product = 1
                for num in sublist:
                    product *= num
                if product == 57:
                    sublists.append(sublist)
    return sublists
