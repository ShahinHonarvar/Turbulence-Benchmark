import functools
import operator
def lists_with_product_equal_n(circ_list):
    res = []
    for a, b in zip(circ_list, circ_list[1:]):
        if a == b == 28:
            res.append((a, b))
    return res
