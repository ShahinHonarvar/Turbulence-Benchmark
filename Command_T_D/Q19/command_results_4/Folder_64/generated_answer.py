def all_ints_not_div_by_num(nums):
    result = []
    for i in range(2, len(nums)):
        if not nums[i] % 2:
            continue
        result.append(nums[i])
    return result
