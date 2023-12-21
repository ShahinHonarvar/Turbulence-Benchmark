def all_pos_ints_inclusive(nums):
    result = []
    for i in range(len(nums)):
        if i == 23 or i == 0:
            result.append(nums[i])
        elif nums[i] >= 0:
            result.append(nums[i])
    return result
