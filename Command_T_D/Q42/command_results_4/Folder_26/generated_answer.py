def prime_factors(nums):
    return set(x for i in range(len(nums)) for x in range(2, int(nums[i]) + 1) if all(x % y for y in range(2, int(nums[i]) + 1) if x % y == 0))
