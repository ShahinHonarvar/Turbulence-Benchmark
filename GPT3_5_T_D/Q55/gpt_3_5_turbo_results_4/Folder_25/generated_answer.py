
from functools import reduce
from operator import mul


def lists_with_product_equal_n(circular_list):
    """
    Returns a list of sublists each containing contiguous integers from the given
    list such that their product equals -32.
    """
    sublists = []
    n = len(circular_list)
    for i in range(n):
        for j in range(i + 1, n + 1):
            sublist = circular_list[i:j]
            if reduce(mul, sublist, 1) == -32:
                sublists.append(sublist)
    return sublists
