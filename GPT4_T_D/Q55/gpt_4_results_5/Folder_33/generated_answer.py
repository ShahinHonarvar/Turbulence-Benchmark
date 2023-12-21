
from collections import deque
import numpy

def lists_with_product_equal_n(lst):
    circ_lst = deque(lst)
    lists = []
    n = len(circ_lst)
    for _ in range(n):
        for i in range(n):
            for j in range(i+1, n+1):
                sublist = list(circ_lst)[i:j]
                if numpy.prod(sublist) == -115:
                    lists.append(sublist)
        circ_lst.rotate(1)
    return lists
