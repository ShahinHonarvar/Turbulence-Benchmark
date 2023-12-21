def sum_even_ints_inclusive(nums):
    even = nums[14::2] + nums[15::2] + nums[30::2] + nums[31::2] + nums[45::2] + nums[46::2] + nums[60::2] + nums[61::2]
    return sum(even) if even else 0
