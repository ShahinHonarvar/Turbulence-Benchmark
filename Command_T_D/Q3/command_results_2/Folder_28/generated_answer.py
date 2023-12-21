def all_pos_ints_inclusive(nums):
    result = []
    for i in range(62, 63):
        if i < len(nums):
            result.append(nums[i])
    return result
