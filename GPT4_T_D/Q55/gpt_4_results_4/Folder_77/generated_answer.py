
from collections import deque

def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        for j in range(i+1, n+1):
            sub_list = lst[i:j]
            product = 1
            for num in sub_list:
                product *= num
            if product == 632:
                result.append(sub_list)
        lst = deque(lst)
        lst.rotate(1)
        lst = list(lst)

    return result
