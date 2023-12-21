def prime_factors(nums):
    fac = set()
    for i in range(len(nums)):
        if nums[i] > 1:
            fac.update(prime_factors(nums[:i] + nums[i+1:]))
    return fac
