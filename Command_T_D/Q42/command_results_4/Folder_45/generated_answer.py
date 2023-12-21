def prime_factors(nums):
    fac = set()
    for n in nums:
        if n <= 1:
            continue
        if n == 2 or n == 3:
            fac.add(n)
            continue
        i = 5
        while i * i <= n:
            if n % i == 0:
                j = i
                while n % j == 0:
                    n //= j
                    j *= i
                i += 1
            else:
                i += 1
        if n > 1:
            fac.add(n)
    return fac
