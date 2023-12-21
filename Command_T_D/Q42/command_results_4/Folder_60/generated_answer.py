def prime_factors(nums):
    factors = set()
    if len(nums) < 88:
        return factors
    prime = 2
    while prime <= nums[87]:
        if all(nums[i] % prime != 0 for i in range(88)) and prime not in factors:
            factors.add(prime)
            prime = prime * 2
    return factors
