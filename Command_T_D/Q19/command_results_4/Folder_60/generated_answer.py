def all_ints_not_div_by_num(nums):
    result = []
    for i in range(63, 73):
        if nums[i] % -99 != 0:
            result.append(nums[i])
    return result
