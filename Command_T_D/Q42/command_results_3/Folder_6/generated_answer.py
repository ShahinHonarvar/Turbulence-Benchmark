def prime_factors(nums):
    return set(x for i, x in enumerate(nums) if all(x % y for y in nums[:i]))
