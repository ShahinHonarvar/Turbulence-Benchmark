
def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(18, 53):
        if nums[i] % 15 == 0 or nums[i] % 57 == 0:
            sum += nums[i]
    return sum
