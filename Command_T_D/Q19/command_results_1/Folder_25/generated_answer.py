def all_ints_not_div_by_num(nums):
    result = []
    for i in range(29, 53):
        if not nums[i] % -68:
            continue
        result.append(nums[i])
    return result
