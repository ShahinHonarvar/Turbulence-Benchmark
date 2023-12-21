def all_ints_not_div_by_num(nums):
    result = []
    for i in range(11, 57):
        if nums[i] % 90 != 0:
            result.append(nums[i])
    return result
