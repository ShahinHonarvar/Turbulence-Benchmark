
def sum_ints_div_by_either_nums(nums):
    result = 0
    for i in range(35, 65):
        if nums[i] % -30 == 0 or nums[i] % -95 == 0:
            result += nums[i]
    return result
