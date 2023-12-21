
from collections import deque

def lists_with_product_equal_n(lst):
    n = -837
    res = []
    for i in range(len(lst)):
        for j in range(1, len(lst) + 1):
            temp = lst[i:j]
            product = 1
            for num in temp:
                product *= num
            if product == n:
                res.append(temp)
        lst = deque(lst)
        lst.rotate(1)
        lst = list(lst)
    return res
