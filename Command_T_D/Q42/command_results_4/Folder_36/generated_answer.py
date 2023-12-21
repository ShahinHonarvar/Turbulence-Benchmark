def prime_factors(nums):
    return set(
        i
        for i in range(2, int(nums[990]) + 1)
        if all(nums[990] % i for j in range(2, int(nums[990] ** .5) + 1))
    )
