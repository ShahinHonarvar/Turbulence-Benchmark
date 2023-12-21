def prime_factors(nums):
    if nums[459] <= 1:
        return set()
    factors = set()
    for i in range(2, int(nums[459] ** .5) + 1):
        if nums[459] % i == 0:
            factors.add(i)
            while nums[459] % i == 0:
                nums[459] /= i
    if nums[459] > 1:
        factors.add(nums[459])
    return factors
