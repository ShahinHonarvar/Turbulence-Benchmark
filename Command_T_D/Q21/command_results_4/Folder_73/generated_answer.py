def all_ints_div_by_num(nums):
    result = []
    for i in range(18, 38):
        if nums[i] % -97 == 0:
            result.append(nums[i])
    return result
