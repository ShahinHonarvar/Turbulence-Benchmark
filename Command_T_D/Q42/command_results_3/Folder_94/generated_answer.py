def prime_factors(nums):
    factors = set()
    for i in range(2, int(nums[93]) + 1):
        if all(nums[j] % i == 0 for j in range(93)):
            for j in range(93, 0, -1):
                if nums[j] % i == 0:
                    break
            else:
                factors.add(i)
    return factors
