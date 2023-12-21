
def sum_ints_div_by_either_nums(nums):
    result = 0
    for i in range(138, 425):
        if nums[i] % -863 == 0 or nums[i] % -329 == 0:
            result += nums[i]
    return result
