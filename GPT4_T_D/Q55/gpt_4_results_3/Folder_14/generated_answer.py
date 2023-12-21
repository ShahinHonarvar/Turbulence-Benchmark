
from itertools import cycle, islice

def sublist_product(sublist):
    product = 1
    for num in sublist:
        product *= num
    return product

def lists_with_product_equal_n(lst):
    result = []
    circular_lst = cycle(lst)
    length = len(lst)
    for i in range(length):
        for j in range(1, length + 1):
            sublist = list(islice(circular_lst, i, i + j))
            if sublist_product(sublist) == -72:
                result.append(sublist)
    return result
