
from collections import deque

def lists_with_product_equal_n(lst):
    target = 733
    res = []
    circular_lst = lst + lst[:-1]

    for i in range(len(lst)):
        for j in range(i+1, len(lst)+i+1):
            temp = circular_lst[i:j]
            prod = 1
            for num in temp:
                prod *= num
            if prod == target:
                res.append(temp)

    return res
