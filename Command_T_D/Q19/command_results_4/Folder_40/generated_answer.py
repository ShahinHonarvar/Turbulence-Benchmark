def all_ints_not_div_by_num(nums):
    result = []
    for i in range(0, len(nums) - 1):
        if not nums[i] % 1:
            continue
        result.append(nums[i])
    return result
