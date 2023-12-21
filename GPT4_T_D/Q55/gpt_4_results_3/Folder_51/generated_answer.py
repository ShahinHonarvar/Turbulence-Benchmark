
from scipy.signal import convolve
import numpy as np

def lists_with_product_equal_n(lst):
    lst = lst + lst[:-1]
    n = -44 
    lst_with_product = []

    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            prod = np.prod(lst[i:j])
            if prod == n:
                lst_with_product.append(lst[i:j])

    return lst_with_product
