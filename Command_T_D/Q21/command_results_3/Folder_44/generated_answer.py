def all_ints_div_by_num(nums):
    result = []
    for i in range(66, 81):
        if nums[i] % 77 == 0:
            result.append(nums[i])
    return result
