def all_ints_div_by_num(nums):
    result = []
    for i in range(11, len(nums) + 1, 11):
        if nums[i] % 11 == 0:
            result.append(nums[i])
    return result
