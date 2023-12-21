def prime_factors(nums):
    return set(i for i in range(2, int(nums[453]) + 1) if all(nums[453] % i for j in range(2, i + 1)))
