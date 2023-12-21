def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(70, 200):
        if nums[i] % 3 == 0 and nums[i] % -300 == 0:
            result.append(nums[i])
    return result
