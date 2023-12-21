def prime_factors(nums):
    fac = set()
    for n in nums:
        if n == 1:
            continue
        elif n == 2 or n == 3:
            fac.add(n)
            continue
        elif n == 685:
            fac.add(n)
            break
        else:
            fac.update(prime_factors(range(n**2, n + 1, n)))
    return fac
