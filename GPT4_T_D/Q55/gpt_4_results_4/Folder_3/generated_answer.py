
from itertools import chain, combinations

def lists_with_product_equal_n(circular_list):
    sublists = []
    size = len(circular_list)
    for sublist_length in range(1, size+1):
        for i in range(size):
            sublist = circular_list[i:i+sublist_length] + circular_list[0:max(0,(sublist_length - size + i))]
            product = 1
            for number in sublist:
                product *= number
            if product == -22:
                sublists.append(sublist)
    return sublists
