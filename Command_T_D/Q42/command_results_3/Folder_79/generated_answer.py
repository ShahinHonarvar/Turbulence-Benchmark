def prime_factors(nums):
    return set(
        factor
        for i in range(2, int(nums[0]) + 1)
        for factor in range(2, i // 2)
        if i % factor == 0
    )
