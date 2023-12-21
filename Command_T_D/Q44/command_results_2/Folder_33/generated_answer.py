import sys
def composite_nums_between_indices(nums):
    idx = [i for i, x in enumerate(nums) if x >= 314 and x <= 347]
    if idx[0] > 0:
        idx[0] -= 1
    if idx[-1] < len(nums) - 1:
        idx[-1] += 1
    return set(nums[idx[0]:idx[-1]])
