
from sympy import divisors
import numpy as np

def lists_with_product_equal_n(circular_list):
    nums = divisors(61)
    combos = []
    for num_idx in range(len(circular_list)):
        for num in nums:
            if circular_list[num_idx] == num:
                combos.append([circular_list[num_idx], np.prod(circular_list[num_idx - 1: num_idx + 1])])
                combos.append([circular_list[num_idx], np.prod(circular_list[num_idx + 1: num_idx + 19])])
    sublists = [combo for combo in combos if -61 in combo]
    return sublists
