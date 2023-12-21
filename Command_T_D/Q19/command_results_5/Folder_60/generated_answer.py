def all_ints_not_div_by_num(nums):
    result = []
    for i in range(63, 73):
        if not nums[i] % -99:
            continue
        result.append(nums[i])
    return result
