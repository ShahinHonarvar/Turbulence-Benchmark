
def sum_ints_div_by_either_nums(nums):
    total = 0
    for i in range(46, 92):
        if nums[i] % 67 == 0 or nums[i] % 15 == 0:
            total += nums[i]
    return total
