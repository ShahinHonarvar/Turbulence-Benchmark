def prime_factors(nums):
    return set(
        (i for i in range(2, int(nums[77]) + 1) if all(nums[77] % i == 0 for j in range(2, int(nums[77]) + 1)))
    )
