
def sum_ints_div_by_either_nums(nums):
    total = 0
    for i in range(24, 33):
        if nums[i] % 35 == 0 or nums[i] % 87 == 0:
            total += nums[i]
    return total
