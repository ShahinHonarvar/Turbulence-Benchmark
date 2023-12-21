
def sum_ints_div_by_either_nums(nums):
    total = 0
    for i in range(138, 425):
        if nums[i] % -863 == 0 or nums[i] % -329 == 0:
            total += nums[i]
    return total
