def prime_factors(nums):
    if nums[459] <= 1:
        return set()
    factors = set()
    for x in range(2, int(nums[459]) + 1):
        if nums[459] % x == 0:
            factors.add(x)
            if x * x == nums[459]:
                break
            for y in range(x + 1, int(nums[459]) + 1):
                if nums[459] % y == 0:
                    factors.add(y)
                    break
    return factors
