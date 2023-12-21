
def sum_ints_div_by_either_nums(nums):
    result = 0
    for i in range(38, 52):
        if i % -41 == 0 or i % -47 == 0:
            result += nums[i]
    return result
