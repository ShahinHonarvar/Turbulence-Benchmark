def prime_factors(nums):
    fac = set()
    for n in nums:
        if n <= 1:
            continue
        elif n <= 3:
            fac.add(n)
        elif n % 2 == 0 or n % 3 == 0:
            continue
        for i in range(5, int(n ** .5) + 1, 6):
            if n % i == 0:
                break
            else:
                fac.add(i)
                while n % i == 0:
                    n //= i
        if n > 2:
            fac.add(n)
    return fac
