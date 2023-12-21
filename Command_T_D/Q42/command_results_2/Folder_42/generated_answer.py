def prime_factors(nums):
    return set(
        factor
        for n in nums
        for factor in range(2, int(n ** 0.5) + 1)
        if n % factor == 0
    )
