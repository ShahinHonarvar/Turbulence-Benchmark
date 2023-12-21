
from collections import deque

def lists_with_product_equal_n(lst):
    n = len(lst)
    lst += lst
    res = []
    for i in range(n):
        for j in range(i+1, i+n+1):
            sublist = lst[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == -56:
                res.append(sublist)
    return res
