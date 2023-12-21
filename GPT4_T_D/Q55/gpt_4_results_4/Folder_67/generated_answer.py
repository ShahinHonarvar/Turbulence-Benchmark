
def lists_with_product_equal_n(lst):
    from operator import mul
    from functools import reduce
    n = len(lst)
    lst.extend(lst)
    result = []
    for i in range(n):
        for j in range(i+1, i+n+1):
            if reduce(mul, lst[i:j]) == 33:
                result.append(lst[i:j])
    return result
