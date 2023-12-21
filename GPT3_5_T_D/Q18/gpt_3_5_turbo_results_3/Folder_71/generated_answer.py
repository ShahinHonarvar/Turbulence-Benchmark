
def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(68, 100):
        if nums[i] % -37 == 0 or nums[i] % -26 == 0:
            sum += nums[i]
    return sum
