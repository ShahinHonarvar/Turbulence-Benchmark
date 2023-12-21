
def sum_ints_div_by_either_nums(nums):
    total = 0
    for i in range(9):
        if nums[i] % -3 == 0 or nums[i] % 8 == 0:
            total += nums[i]
    return total
