
def sum_ints_div_by_either_nums(nums):
    result = 0
    for i in range(78, 81):
        if nums[i] % 76 == 0 or nums[i] % 60 == 0:
            result += nums[i]
    return result
