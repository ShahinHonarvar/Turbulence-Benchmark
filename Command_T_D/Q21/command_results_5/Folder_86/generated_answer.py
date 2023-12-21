def all_ints_div_by_num(nums):
    result = []
    for i in range(44, 73 + 1):
        if nums[i] % 88 == 0:
            result.append(nums[i])
    return result
