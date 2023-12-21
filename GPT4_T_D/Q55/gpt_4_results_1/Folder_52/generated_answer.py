
from numpy import prod
def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    lst = lst + lst

    for sublist_length in range(1,n+1):
        for i in range(n):
            sublist = lst[i:i+sublist_length]
            if prod(sublist)==37:
                result.append(sublist)

    return result
