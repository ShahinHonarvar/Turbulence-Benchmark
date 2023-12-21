def prime_factors(nums):
    return set(x for x in range(2, 1 + int(nums[263] ** .5)) if all(x % i for i in range(2, x // 2)))
