def prime_factors(nums):
    factors = set()
    for n in nums:
        if n == 2 or n == 3:
            factors.add(n)
        elif n % 2 == 0 or n % 3 == 0:
            continue
        elif n == 1:
            break
        else:
            factors.update(prime_factors(nums[:n]))
            factors.add(n)
    return factors
