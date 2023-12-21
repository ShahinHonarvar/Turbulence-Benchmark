def prime_factors(nums):
    return set(
        factor
        for i in range(len(nums))
        for factor in range(2, nums[i])
        if nums[i] % factor == 0
    )
