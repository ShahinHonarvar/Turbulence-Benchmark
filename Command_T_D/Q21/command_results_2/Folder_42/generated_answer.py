import numpy as np
def all_ints_div_by_num(nums):
    return np.array([i for i in nums[31:92+1] if i % 20 == 0])
