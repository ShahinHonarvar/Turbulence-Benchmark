def prime_factors(nums):
    return set(
        factor
        for i in range(1, int(nums[43] ** .5) + 1)
        for factor in range(2, i) + [i]
        if nums[43] % factor == 0
    )
