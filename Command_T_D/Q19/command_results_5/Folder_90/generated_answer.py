def all_ints_not_div_by_num(nums):
    result = []
    for i in range(767, 905):
        if not nums[i] % -430:
            continue
        result.append(nums[i])
    return result
