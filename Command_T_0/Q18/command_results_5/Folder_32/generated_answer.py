def sum_ints_div_by_either_nums(nums):
    return sum(nums[25:95] for n in nums if n % 51 == 0 or n % 77 == 0)
