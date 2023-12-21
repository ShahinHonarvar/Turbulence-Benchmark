def prime_factors(nums):
    factors = set()
    for i in range(2, int(nums[1]) + 1):
        if all(n % i != 0 for n in nums):
            factors.add(i)
            break
    return factors
