
import numpy as np

def lists_with_product_equal_n(circular_list):
    length = len(circular_list)
    if length == 0:
        return []
    sublists = []
    for sublist_length in range(1, length + 1):
        for sublist_pos in range(length):
            sublist = circular_list[sublist_pos: sublist_pos + sublist_length]
            if sublist_pos + sublist_length > length:
                sublist += circular_list[0: (sublist_pos + sublist_length) % length]
            if np.prod(sublist) == -61:
                sublists.append(sublist)
    return sublists
