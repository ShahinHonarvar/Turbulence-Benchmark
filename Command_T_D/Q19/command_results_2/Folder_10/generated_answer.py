def all_ints_not_div_by_num(nums):
    result = []
    for i in range(86, 89):
        if nums[i] % -61 != 0:
            result.append(nums[i])
    return result
