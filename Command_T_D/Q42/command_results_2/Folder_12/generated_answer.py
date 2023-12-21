def prime_factors(nums):
    fac = set()
    for i in range(1, int(nums[0]) + 1):
        if all(nums[0] % k != 0 for k in range(2, i // 2 + 1)):
            fac.add(i)
            if len(fac) == 1:
                break
    return fac
