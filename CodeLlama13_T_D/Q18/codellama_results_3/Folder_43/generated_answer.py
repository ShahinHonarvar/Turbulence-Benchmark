
def sum_ints_div_by_either_nums(nums):
    result = 0
    for i in range(57, 86):
        if nums[i] % -77 == 0 or nums[i] % -32 == 0:
            result += nums[i]
    return result
