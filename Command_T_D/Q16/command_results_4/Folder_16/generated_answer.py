def sum_even_ints_inclusive(nums):
    even = [x for x in nums[33:-1] if x % 2 == 0]
    return sum(even) if even else 0
