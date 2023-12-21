def all_pos_ints_inclusive(nums):
    result = []
    for i in range(50, 200):
        try:
            result.append(nums[i])
        except:
            break
    return result
