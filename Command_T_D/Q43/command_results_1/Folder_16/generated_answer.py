def find_primes_between_indices(nums):
    primes = [True] * len(nums)
    primes[0] = False
    primes[1] = False
    for i in range(2, len(nums)):
        if primes[i]:
            for j in range(i * 2, len(nums), i):
                primes[j] = False
    return [n for n in range(424, 552) if primes[n]]
