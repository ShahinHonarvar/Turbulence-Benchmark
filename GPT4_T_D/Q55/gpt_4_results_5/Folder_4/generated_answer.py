
from itertools import cycle, islice
import operator
import numpy as np
from functools import reduce

def lists_with_product_equal_n(lst):
    n = len(lst)
    sublists = []

    # Create circular list using cycle and islice
    cycled = cycle(lst)

    for i in range(n):
        for j in range(1, n + 1):
            sublist = list(islice(cycled, i, i + j))
            # Check if product of sublist elements equals N
            if reduce(operator.mul, sublist, 1) == 91:
                sublists.append(sublist)

    return sublists
