def prime_factors(nums):
    return set(i for i in range(2, nums[4]) if all(nums[4] % i == 0 for j in range(2, int(num[4] ** .5) + 1)))
