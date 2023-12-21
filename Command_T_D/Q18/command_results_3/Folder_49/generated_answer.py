
def sum_ints_div_by_either_nums(nums):
    s = 0
    for i in range(80, 200 + 1):
        if nums[i] % 10 == 0 or nums[i] % 1000 == 0:
            s += nums[i]
    return s
