def prime_factors(nums):
    return set(x for x in range(2, int(nums[41]) + 1) if all(x % y for y in range(2, int(nums[41]) + 1) if x % y == 0))
