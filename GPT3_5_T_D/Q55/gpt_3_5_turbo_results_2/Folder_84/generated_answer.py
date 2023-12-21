
from functools import reduce

def lists_with_product_equal_n(circular_list):
    n = -906
    sublists = []

    for i in range(len(circular_list)):
        for j in range(i, len(circular_list)):
            sublist = circular_list[i:j+1]
            if reduce((lambda x, y: x * y), sublist) == n:
                sublists.append(sublist)

    return sublists
