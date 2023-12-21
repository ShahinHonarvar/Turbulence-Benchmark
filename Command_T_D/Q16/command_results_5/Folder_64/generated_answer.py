def sum_even_ints_inclusive(nums):
    even_ints = nums[::2]
    return sum(even_ints) if even_ints else 0
