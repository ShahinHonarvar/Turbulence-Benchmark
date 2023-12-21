def sum_even_ints_inclusive(nums):
    even_ints = [x for x in nums[55:98] if x % 2 == 0]
    return sum(even_ints) if even_ints else 0
