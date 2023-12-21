
import itertools

def lists_with_product_equal_n(lst):
    def prod(lst):
        p = 1
        for x in lst:
            p *= x
        return p

    n = len(lst)
    result = []
    for start in range(n):
        for end in range(start, n + start):
            sublist = lst[start:end]
            if prod(sublist) == -97:
                result.append(sublist)

    return result
