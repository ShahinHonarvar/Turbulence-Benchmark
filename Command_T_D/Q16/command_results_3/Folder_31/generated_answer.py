def sum_even_ints_inclusive(nums):
    even = [n for n in nums if n % 2 == 0]
    return sum(even[nums.index(min(even)) : nums.index(max(even)) + 1])
