def prime_factors(nums):
    factors = set()
    for i in range(2, int(nums[16]) + 1):
        if nums[16] % i == 0:
            factors.add(i)
            while nums[16] % i == 0:
                nums[16] /= i
    if nums[16] != 1:
        factors.add(nums[16])
    return factors
