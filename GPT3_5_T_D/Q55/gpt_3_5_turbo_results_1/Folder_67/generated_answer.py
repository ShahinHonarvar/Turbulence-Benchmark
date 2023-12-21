
from math import prod
def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for i in range(n):
        for j in range(i, i + n):
            sublist = circular_list[i:j]
            if prod(sublist) == 33:
                result.append(sublist)
    return result
