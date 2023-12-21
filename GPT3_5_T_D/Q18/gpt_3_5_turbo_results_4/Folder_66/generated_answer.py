
def sum_ints_div_by_either_nums(nums):
    total = 0
    for i in range(58, 82):
        if nums[i] % 55 == 0 or nums[i] % 10 == 0:
            total += nums[i]
    return total
