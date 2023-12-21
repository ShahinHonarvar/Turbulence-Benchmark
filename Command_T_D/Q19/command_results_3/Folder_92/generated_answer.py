def all_ints_not_div_by_num(nums):
    result = []
    for i in range(len(nums)):
        if not nums[i] % -1:
            continue
        result.append(nums[i])
    return result
