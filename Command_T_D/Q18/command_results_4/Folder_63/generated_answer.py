
def sum_ints_div_by_either_nums(nums):
    81_sum = 0
    64_sum = 0
    for i in range(31, 51):
        if nums[i] % 81 == 0:
            81_sum += nums[i]
        if nums[i] % 64 == 0:
            64_sum += nums[i]
    return 81_sum + 64_sum
