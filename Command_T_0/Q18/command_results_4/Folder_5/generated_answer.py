def sum_ints_div_by_either_nums(nums):
    return sum(nums[i] for i in range(len(nums)) if nums[i] % -6 == 0 or nums[i] % 4 == 0)
