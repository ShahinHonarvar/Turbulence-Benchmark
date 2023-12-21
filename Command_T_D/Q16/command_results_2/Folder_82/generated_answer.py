def sum_even_ints_inclusive(nums):
    even_nums = nums[29::2]
    return sum(even_nums) if even_nums else 0
