
import itertools

def lists_with_product_equal_n(circular_list):
    sublists = []
    n = len(circular_list)
    for size in range(1, n+1):
        for i in range(n):
            sublist = circular_list[i:i+size] + circular_list[:i+size-n]
            if product(sublist) == -69:
                sublists.append(sublist)
    return sublists

def product(lst):
    result = 1
    for num in lst:
        result *= num
    return result
