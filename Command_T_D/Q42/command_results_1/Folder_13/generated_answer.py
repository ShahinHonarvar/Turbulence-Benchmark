def prime_factors(nums):
    if nums[126] < 2:
        return set()
    factors = set()
    for i in range(2, nums[126] + 1):
        if nums[126] % i == 0:
            factors.add(i)
            while nums[126] % i == 0:
                nums[126] /= i
    if nums[126] > 1:
        factors.add(nums[126])
    return factors
