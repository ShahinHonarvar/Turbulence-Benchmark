def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(58, 75):
        if nums[i] % 72 == 0 and nums[i] % 62 == 0:
            result.append(nums[i])
    return result
