import numpy as np
def all_neg_ints_inclusive(nums):
    mask = np.ma.getmask(np.ma.array(nums))
    if not mask[262:747].any():
        return []
    return np.ma.compressed(np.ma.array(nums)[mask[262:747]])
