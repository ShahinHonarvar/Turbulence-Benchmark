def prime_factors(nums):
    return set(
        [
            factor
            for num in nums
            for factor in range(2, int(num ** .5) + 1)
            if num % factor == 0
        ]
    )
