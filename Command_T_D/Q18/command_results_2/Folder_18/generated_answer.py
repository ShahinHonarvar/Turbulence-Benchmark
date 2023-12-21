
def sum_ints_div_by_either_nums(nums):
    s = 0
    for i in range(55, 67):
        if nums[i] % 22 == 0 or nums[i] % 82 == 0:
            s += nums[i]
    return s
