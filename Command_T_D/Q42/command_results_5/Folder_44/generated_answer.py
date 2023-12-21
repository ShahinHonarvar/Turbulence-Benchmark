def prime_factors(nums):
    if len(nums) == 0:
        return set()
    if len(nums) == 1:
        return set(nums)
    factors = set()
    for n in nums:
        if n == 1:
            continue
        if n == 2 or n == 3:
            factors.add(n)
            continue
        if n == 4:
            factors.add(2)
            factors.add(2)
            continue
        for d in range(5, int(n ** .5) + 1):
            if n % d == 0:
                factors.add(d)
                n /= d
                break
    return factors
