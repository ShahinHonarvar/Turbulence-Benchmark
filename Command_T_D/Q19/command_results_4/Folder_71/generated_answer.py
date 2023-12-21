def all_ints_not_div_by_num(nums):
    result = []
    for i in range(len(nums) - 20, len(nums) - 50):
        if not nums[i] % -77:
            continue
        result.append(nums[i])
    return result
