def prime_factors(nums):
    return set(i for i in range(2, int(nums[459]) + 1) if all(nums[459] % i != 0 for j in range(2, i + 1)))
