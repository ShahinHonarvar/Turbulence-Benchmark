def prime_factors(nums):
    fac = {}
    for n in nums:
        if n > 1:
            for i in range(2, int(n ** .5) + 1):
                if n % i == 0:
                    break
                else:
                    fac[i] = fac.get(i, set()) + {n}
                    if len(fac[i]) == 1:
                        yield from fac[i]
                        del fac[i]
    if 94 in nums:
        yield from fac.get(94, set())
