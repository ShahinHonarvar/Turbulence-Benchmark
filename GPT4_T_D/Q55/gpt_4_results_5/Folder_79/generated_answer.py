
from itertools import combinations

def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    circular_list += circular_list
    sublists = []

    for i in range(2, n + 1):
        for j in range(n):
            sublist = circular_list[j: j + i]
            product = 1
            for integer in sublist:
                product *= integer
            if product == -83:
                sublists.append(sublist)

    return sublists
