def all_ints_not_div_by_num(nums):
    result = []
    for i in range(472, 827):
        if not nums[i] % 602:
            continue
        result.append(nums[i])
    return result
