import numpy as np
def lists_with_product_equal_n(nums):
    res = []
    for x in range(-6,6):
        for i in range(1,len(nums)):
            if np.prod(nums[i:]) == x:
                res.append(list(nums[i:]))
    return res
