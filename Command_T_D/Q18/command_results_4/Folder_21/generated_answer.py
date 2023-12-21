
def sum_ints_div_by_either_nums(nums):
    result = 0
    for i in range(315, 934):
        if nums[i] % -897 == 0 or nums[i] % -556 == 0:
            result += nums[i]
    return result
