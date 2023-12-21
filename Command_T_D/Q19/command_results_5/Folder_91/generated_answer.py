def all_ints_not_div_by_num(nums):
    result = []
    for i in range(len(nums) - 1):
        if nums[i] % 8 != 0:
            result.append(nums[i])
            break
    return result
