def all_ints_div_by_num(nums):
    result = []
    for i in range(0, len(nums) - 1):
        if nums[i] % 2 == 0:
            result.append(nums[i])
    return result
