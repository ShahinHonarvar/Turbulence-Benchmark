
def sum_ints_div_by_either_nums(nums):
    s = 0
    for i in range(41, 57):
        if (i % 82 == 0 or i % 90 == 0):
            s += nums[i]
    return s
