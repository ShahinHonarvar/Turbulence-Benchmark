
from itertools import cycle
def lists_with_product_equal_n(lst):
    n = -82
    sublists = []
    for start_index in range(len(lst)):
        for sublist_len in range(1, len(lst) + 1):
            sublist = lst[start_index:start_index + sublist_len]
            if len(sublist) < sublist_len:
                sublist = list(cycle(lst))[start_index:start_index + sublist_len]
            product = 1
            for num in sublist:
                product *= num
            if product == n:
                sublists.append(sublist)
    return sublists
