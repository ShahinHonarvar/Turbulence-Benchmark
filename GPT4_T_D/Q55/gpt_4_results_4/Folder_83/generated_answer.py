
from math import prod

def lists_with_product_equal_n(circ_list):
    result = []
    length = len(circ_list)

    for sublist_len in range(1, length+1):
        for start_index in range(length):
            sublist = [circ_list[(start_index+i) % length] for i in range(sublist_len)]
            if prod(sublist) == -57:
                result.append(sublist)
                
    return result
