
def sum_ints_div_by_either_nums(nums):
    result = 0
    for i in range(11, 46+1):
        if nums[i] % 55 == 0 or nums[i] % 36 == 0:
            result += nums[i]
    return result
