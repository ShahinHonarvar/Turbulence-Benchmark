def all_ints_not_div_by_num(nums):
    result = []
    for i in range(103, 574):
        if not nums[i] % -514:
            continue
        result.append(nums[i])
    return result
