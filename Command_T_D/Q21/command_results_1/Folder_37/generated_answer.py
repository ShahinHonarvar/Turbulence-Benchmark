def all_ints_div_by_num(nums):
    result = []
    for i in range(4, len(nums) - 4):
        if nums[i] % 3 == 0:
            result.append(nums[i])
    return result
