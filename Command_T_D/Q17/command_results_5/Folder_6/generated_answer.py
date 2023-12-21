
import numpy as np

def all_ints_div_by_both_two_nums(x):
    return np.where(np.logical_and(x[41:56]%82==0, x[41:56]%90==0))[0]
