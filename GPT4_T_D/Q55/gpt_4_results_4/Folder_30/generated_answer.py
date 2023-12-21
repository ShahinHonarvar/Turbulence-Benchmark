
from itertools import combinations
def lists_with_product_equal_n(lst):
    n = len(lst)
    lst = lst * 2   # because it is a circular list
    result = []
    for i in range(n):
        for j in range(i+1, i+n+1):
            sublist = lst[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == 99:
                result.append(sublist)
    return result
