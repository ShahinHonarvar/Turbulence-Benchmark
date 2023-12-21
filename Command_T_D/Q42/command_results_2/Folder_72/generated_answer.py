def prime_factors(nums):
    return set(int(x) for x in range(2, int(nums[16]) + 1) if all(x % y == 0 for y in range(2, int(x ** .5) + 1)))
