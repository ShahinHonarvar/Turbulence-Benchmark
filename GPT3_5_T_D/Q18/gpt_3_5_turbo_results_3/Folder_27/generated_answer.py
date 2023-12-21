
def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(20, 36):
        if nums[i] % -36 == 0 or nums[i] % -89 == 0:
            sum += nums[i]
    return sum
