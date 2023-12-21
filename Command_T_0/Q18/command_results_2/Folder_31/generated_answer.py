def sum_ints_div_by_either_nums(nums):
    return sum(nums[56:88] if n % -59 == 0 or n % -79 == 0 else 0 for n in nums)
