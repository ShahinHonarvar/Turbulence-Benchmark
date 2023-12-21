def all_ints_not_div_by_num(nums):
    num_range = range(70, 200)
    return [nums[i] for i in num_range if nums[i] % -300 != 0]
