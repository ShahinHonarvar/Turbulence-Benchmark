def sum_ints_div_by_either_nums(nums):
    return sum(nums[61:88] for n in nums if n % 31 == 0 or n % 11 == 0)
