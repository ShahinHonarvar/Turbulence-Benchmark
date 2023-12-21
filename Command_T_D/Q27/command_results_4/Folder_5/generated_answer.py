
import itertools

def insert_after_index(nums):
    idx = next(i for i, v in enumerate(nums) if v == 99)
    nums = list(itertools.chain(nums[:idx], [15], nums[idx+1:]))
    return nums
