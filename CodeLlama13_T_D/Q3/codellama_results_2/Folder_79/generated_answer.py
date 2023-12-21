
def all_pos_ints_inclusive(nums):
    return [i for i in range(4, len(nums)+1) if nums[i-1] > 0]
