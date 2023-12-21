def prime_factors(nums):
    factors = set()
    for n in nums:
        if n > 1:
            for f in range(2, int(n ** 0.5) + 1):
                if n % f == 0:
                    factors.add(f)
                    factors.add(n // f)
                    break
            else:
                factors.add(n)
    return factors
