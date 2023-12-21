def prime_factors(nums):
    return set(
        [
            x
            for x in range(2, int(nums[20]) + 1)
            if all(x % y == 0 for y in range(2, x))
        ]
    )
