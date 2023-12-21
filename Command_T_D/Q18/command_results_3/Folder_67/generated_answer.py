
def sum_ints_div_by_either_nums(nums):
    result = 0
    for i in range(24, 33):
        if (i % 35 == 0 or i % 87 == 0):
            result += nums[i]
    return result
