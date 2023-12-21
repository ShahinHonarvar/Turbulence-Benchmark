
from functools import reduce
from operator import mul

def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for i in range(n):
        for j in range(i, n):
            sub_lst = lst[i:j+1] + lst[:j+1-(n-i)] if j+1-(n-i) > 0 else lst[i:j+1]
            product = reduce(mul, sub_lst)
            if product == 733:
                result.append(sub_lst)
    return result
