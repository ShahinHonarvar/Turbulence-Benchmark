
def all_pos_ints_inclusive(nums):
    result = []
    for i in range(64, 67):
        if i < len(nums) and nums[i] > 0:
            result.append(nums[i])
    return result
