def sum_ints_div_by_either_nums(nums):
    return sum(nums[i] for i in range(0, 10) if nums[i] % 10 == 0 or nums[i] % 100 == 0)
