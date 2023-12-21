def prime_factors(nums):
    factors = set()
    for i in range(1, len(nums) + 1):
        if nums[i - 1] % i == 0:
            for j in range(2, i):
                if nums[i - 1] % j == 0:
                    break
            else:
                factors.add(i)
    return factors
