
from collections import deque

def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        for j in range(i+1, n+1):
            sublist = lst[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == 13:
                result.append(sublist)
        lst = deque(lst)
        lst.rotate(1)
        lst = list(lst)
    return result
