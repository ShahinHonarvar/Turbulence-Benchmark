
from itertools import chain, combinations

def lists_with_product_equal_n(lst):
    product_lists = []
    n = len(lst)
    circular_lst = lst * 2
    for length in range(1, n+1):
        for start in range(n):
            sublist = circular_lst[start:start+length]
            prod = 1
            for ele in sublist:
                prod *= ele
            if prod == -115:
                product_lists.append(sublist)
    return product_lists
