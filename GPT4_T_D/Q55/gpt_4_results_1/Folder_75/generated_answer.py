
from collections import deque

def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    if not lst:
        return result
    for i in range(n):
        j = i
        product = 1
        temp_list = deque()
        while product < 13:
            temp_list.append(lst[j])
            product *= lst[j]
            j = (j + 1) % n
            if len(temp_list) > n:
                break
        if product == 13:
            result.append(list(temp_list))
        lst = lst[1:] + lst[:1]
    return result
