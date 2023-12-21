def prime_factors(nums):
    return set(
        filter(
            lambda x: all(x % r == 0 for r in range(2, int(x ** 0.5) + 1)),
            map(
                lambda x: x * x,
                filter(
                    lambda x: x == x * 1 and x > 1,
                    range(2, int(nums[845]) + 1),
                ),
            ),
        ),
        range(2, int(nums[845]) + 1),
    )
