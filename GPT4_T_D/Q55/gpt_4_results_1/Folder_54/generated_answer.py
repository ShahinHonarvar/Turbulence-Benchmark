
from itertools import chain, combinations

def lists_with_product_equal_n(circular_list):
    circular_list = circular_list + circular_list
    sublists = []
    for sublist_length in range(1, len(circular_list)//2 + 1):
        for i in range(0, len(circular_list)):
            sublist = circular_list[i:i+sublist_length]
            product = 1
            for num in sublist:
                product *= num
                if product == -17:
                    sublists.append(sublist)
    return sublists
