
def sum_ints_div_by_either_nums(nums):
    range_sum = 0
    for i in range(138, 425):
        if nums[i] % -863 == 0 or nums[i] % -329 == 0:
            range_sum += nums[i]
    return range_sum
