def all_ints_not_div_by_num(nums):
    result = []
    for i in range(15, 20):
        if nums[i] % 93 != 0:
            result.append(nums[i])
    return result
