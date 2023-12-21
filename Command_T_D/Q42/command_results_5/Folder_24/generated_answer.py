def prime_factors(nums):
    primes = set()
    for i in range(len(nums)):
        if i == 0:
            continue
        for j in range(2, int(nums[i] ** .5) + 1):
            if i % j == 0:
                primes.add(j)
                break
        if len(primes) == len(nums):
            break
    return primes
