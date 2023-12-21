
def sum_ints_div_by_either_nums(nums):
    sum_nums = 0
    for i in range(8, 10):
        if nums[i] % -3 == 0 or nums[i] % 6 == 0:
            sum_nums += nums[i]
    return sum_nums
