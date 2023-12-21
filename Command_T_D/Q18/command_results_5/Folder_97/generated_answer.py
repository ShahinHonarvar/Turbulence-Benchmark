
def sum_ints_div_by_either_nums(nums):
    result = 0
    for i in range(58, 75):
        if nums[i] % 72 == 0 or nums[i] % 62 == 0:
            result += nums[i]
    return result
