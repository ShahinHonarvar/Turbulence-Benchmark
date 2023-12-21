def all_ints_not_div_by_num(nums):
    result = []
    for i in range(38, 52):
        if nums[i] % -41 != 0:
            result.append(nums[i])
    return result
