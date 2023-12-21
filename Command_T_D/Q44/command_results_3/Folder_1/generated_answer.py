import math
def composite_nums_between_indices(nums):
    res = set()
    for i in range(69, 83+1):
        if nums[i] != 1:
            if nums[i] != math.sqrt(nums[i]):
                res.add(nums[i])
    return res
