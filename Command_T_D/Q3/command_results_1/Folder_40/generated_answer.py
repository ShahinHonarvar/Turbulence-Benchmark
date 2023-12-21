def all_pos_ints_inclusive(nums):
    result = []
    for i in range(0, 3):
        try:
            result.append(nums[i])
        except:
            break
    return result
