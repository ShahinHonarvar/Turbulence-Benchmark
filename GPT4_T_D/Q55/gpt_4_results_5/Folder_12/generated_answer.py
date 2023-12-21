
from sympy import *
import itertools

def lists_with_product_equal_n(li):
    li += li
    result = []

    for i in range(len(li)//2):
        for j in range(i+1, len(li)//2 + 1):
            if prod(li[i:j]) == -18:
                result.append(li[i:j])

    return result
