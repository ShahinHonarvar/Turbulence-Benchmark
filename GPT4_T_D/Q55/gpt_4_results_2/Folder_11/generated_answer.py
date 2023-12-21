
from collections import deque
def lists_with_product_equal_n(circular_list):
    res = []
    n = len(circular_list)
    for i in range(n):
        for j in range(i+1, n+1):
            sub_list = list(circular_list)[i:j]
            product = 1
            for k in sub_list:
                product *= k
            if product == -15:
                res.append(sub_list)
        circular_list.rotate(-1)
    return res
