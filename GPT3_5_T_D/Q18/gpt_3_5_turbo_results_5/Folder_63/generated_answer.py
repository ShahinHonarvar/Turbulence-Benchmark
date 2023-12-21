
def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(31, 51):
        if nums[i] % 81 == 0 or nums[i] % 64 == 0:
            sum += nums[i]
    return sum
