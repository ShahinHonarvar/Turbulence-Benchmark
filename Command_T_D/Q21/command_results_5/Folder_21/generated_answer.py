import numpy as np
def all_ints_div_by_num(nums):
    return np.where(np.mod(np.array(nums)[572:806+1], -158) == 0)[0]
