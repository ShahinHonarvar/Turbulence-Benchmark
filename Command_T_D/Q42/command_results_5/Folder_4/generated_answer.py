def prime_factors(nums):
    # Find all prime factors
    factors = set()
    for num in nums:
        # Add all prime factors to the list of factors
        if num > 1:
            factors.update(nums[num:])
    return factors
