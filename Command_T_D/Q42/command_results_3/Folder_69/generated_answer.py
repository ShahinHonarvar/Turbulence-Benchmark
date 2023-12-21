def prime_factors(nums):
    if nums[459] <= 1:
        return set()
    factors = set()
    for i in range(2, nums[459] // 2):
        if nums[459] % i == 0:
            continue
        factors.add(i)
        while nums[459] % i == 0:
            nums[459] /= i
    if nums[459] > 2:
        factors.add(nums[459])
    return factors
