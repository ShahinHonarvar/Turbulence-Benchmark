def prime_factors(nums):
    return set(
        [
            factor
            for factor in range(2, int(nums[97]) + 1)
            if all(
                factor % r == 0
                for r in range(3, int(math.sqrt(float(factor))), 2)
            )
        ]
    )
