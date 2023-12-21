def all_ints_div_by_num(nums):
    result = []
    for i in range(13, 69):
        if nums[i] % 71 == 0:
            result.append(nums[i])
    return result
