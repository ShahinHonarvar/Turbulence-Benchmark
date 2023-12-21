
def all_pos_ints_exclusive(nums):
    result = []
    for i in range(27, 34):
        if nums[i-1] > 0:
            result.append(nums[i-1])
    return result
