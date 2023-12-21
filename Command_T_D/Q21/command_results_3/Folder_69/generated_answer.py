def all_ints_div_by_num(nums):
    result = []
    for i in range(43, 76 + 1):
        if nums[i] % 14 == 0:
            result.append(nums[i])
    return result
