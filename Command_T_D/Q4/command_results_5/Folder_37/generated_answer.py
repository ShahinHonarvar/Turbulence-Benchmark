def all_pos_ints_exclusive(nums):
    result = []
    for i in range(1, len(nums) + 1):
        if i > 0 and i < len(nums) and nums[i-1] <= 0 and nums[i] > 0:
            result.append(nums[i])
    return result
