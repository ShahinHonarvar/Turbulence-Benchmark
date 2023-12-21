def all_ints_div_by_num(nums):
    result = []
    for i in range(59, 79 + 1):
        if nums[i] % -82 == 0:
            result.append(nums[i])
    return result
