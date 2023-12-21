
def sum_ints_div_by_either_nums(nums):
    result = 0
    for i in range(14, 94):
        if nums[i] % 71 == 0 or nums[i] % 81 == 0:
            result += nums[i]
    return result
