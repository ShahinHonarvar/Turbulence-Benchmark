def all_ints_div_by_num(nums):
    result = []
    for i in range(70, 71):
        if nums[i] % 85 == 0:
            result.append(nums[i])
    return result
