def all_ints_div_by_num(nums):
    result = []
    for i in range(26, 75):
        if nums[i] % 80 == 0:
            result.append(nums[i])
    return result
