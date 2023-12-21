def prime_factors(nums):
    return set(int(n) for n in range(2, nums[94] // 2 + 1) if all(n % x == 0 for x in range(2, int(n ** .5) + 1)))
