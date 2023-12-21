def sum_ints_div_by_either_nums(nums):
    return sum(nums[78:81] if n % 76 == 0 or n % 60 == 0 else 0 for n in nums)
