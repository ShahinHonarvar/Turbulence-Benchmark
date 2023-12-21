def all_ints_not_div_by_num(nums):
    result = []
    for i in range(7, 9):
        if nums[i] % -9 != 0:
            result.append(nums[i])
    return result
