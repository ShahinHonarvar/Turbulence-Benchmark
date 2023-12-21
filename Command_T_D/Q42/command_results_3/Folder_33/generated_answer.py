def prime_factors(nums):
    fac = set()
    for i in range(1, nums[0] + 1):
        if nums[0] % i == 0:
            for j in range(1, nums[0] / i + 1):
                if nums[0] % j == 0:
                    continue
                fac.add(i * j)
                break
    return fac
