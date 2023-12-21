
from collections import deque
from functools import reduce
from operator import mul
import numpy as np

def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    product_target = -938
    sublists = []

    for l in range(1, n+1):
        circular_deque = deque(circular_list)
        for i in range(n):
            sublist = list(np.roll(circular_deque, -i)[:l])
            if reduce(mul, sublist, 1) == product_target:
                sublists.append(sublist)
                
    return sublists
