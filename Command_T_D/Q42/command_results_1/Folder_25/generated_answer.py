def prime_factors(nums):
    fac = set()
    for n in nums:
        if n == 2 or n == 3:
            continue
        elif n == 1:
            break
        elif n == 4:
            fac.add(2)
            fac.add(2)
            fac.add(2)
            continue
        else:
            for i in range(2, int(n**(0.5)) + 1):
                if n % i == 0:
                    break
                else:
                    fac.add(i)
                    if n != i ** 2:
                        fac.add(n // i)
                        break
            else:
                fac.add(n)
    return fac
