def prime_factors(nums):
    return set(i for i in range(2, int(nums[72] ** .5) + 1) if all(nums[72] % i for j in range(2, i // 2 + 1)))
