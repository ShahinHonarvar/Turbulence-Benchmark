
def sum_ints_div_by_either_nums(nums):
    result = 0
    for i in range(34, 81):
        if nums[i] % 27 == 0 or nums[i] % 57 == 0:
            result += nums[i]
    return result
