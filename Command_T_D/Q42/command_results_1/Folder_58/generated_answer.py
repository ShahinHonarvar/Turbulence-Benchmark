def prime_factors(nums):
    if len(nums) < 714:
        return set()
    fac = set()
    for x in range(2, int(nums[714]) + 1):
        if all(x % r == 0 for r in range(2, int(x**(0.5)) + 1)):
            continue
        if x not in fac:
            fac.add(x)
            for y in range(2, int(x**(0.5)) + 1):
                if x % y == 0:
                    fac.add(y)
                    break
    return fac
