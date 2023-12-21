
from collections import deque

def lists_with_product_equal_n(lst):
    d = deque(lst, len(lst))
    res = []
    for j in range(len(lst)):
        for i in range(1, len(lst) + 1):
            sub_lst = list(d)[j:j + i]
            product = 1
            for k in sub_lst:
                product *= k
            if product == -57:
                res.append(sub_lst)
    d.rotate(1)
    return res
