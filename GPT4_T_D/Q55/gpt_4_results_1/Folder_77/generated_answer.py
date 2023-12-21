
from collections import deque

def lists_with_product_equal_n(circular_list):
    res = []
    n = len(circular_list)
    circular_list.extend(circular_list)
    for i in range(n):
        for j in range(i+1, i+n+1):
            sub_list = circular_list[i:j]
            product = 1
            for number in sub_list:
                product *= number
            if product == 632:
                res.append(list(deque(sub_list)))
    return res
