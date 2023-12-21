def all_ints_not_div_by_num(nums):
    result = []
    for i in range(41, 69):
        if not nums[i] % -82:
            break
        result.append(nums[i])
    return result
