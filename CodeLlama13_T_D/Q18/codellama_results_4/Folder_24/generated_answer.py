
def sum_ints_div_by_either_nums(nums):
    result = 0
    for i in range(29, 54):
        if nums[i] % -68 == 0 or nums[i] % -85 == 0:
            result += nums[i]
    return result
