def sum_even_ints_inclusive(nums):
    even_ints = list(range(min(nums), max(nums)+1, 2))
    return sum(nums[even_ints[0]:even_ints[-1]+1])
