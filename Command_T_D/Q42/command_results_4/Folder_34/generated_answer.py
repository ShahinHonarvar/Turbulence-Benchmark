def prime_factors(nums):
    fac = set()
    for n in nums:
        if n == 1:
            continue
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                fac.update(prime_factors(nums[:n]))
                break
        else:
            fac.add(n)
    return fac
