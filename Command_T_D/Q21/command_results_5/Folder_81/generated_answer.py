def all_ints_div_by_num(nums):
    result = []
    for i in range(0, 3):
        if i in nums:
            result.append(nums[i])
    return result
