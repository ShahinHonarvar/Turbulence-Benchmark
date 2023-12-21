
from itertools import chain, combinations
from math import prod

def lists_with_product_equal_n(integers):
    def powerset(iterable):
        s = list(iterable)
        return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

    sublists = []
    for subset in powerset(integers):
        if prod(subset) == 5:
            sublists.append(list(subset))
    return sublists
