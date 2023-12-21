def prime_factors(nums):
    factors = set()
    for i in range(1, int(nums[77]) + 1):
        if all(nums[j] % i != 0 for j in range(1, len(nums))):
            factors.add(i)
    return factors
