def all_ints_div_by_num(nums):
    result = []
    for i in range(17, 63):
        if nums[i] % 89 == 0:
            result.append(nums[i])
    return result
