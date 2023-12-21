def find_primes_between_indices(nums):
    primes = []
    for n in nums:
        if all(n % d for d in range(3, 1 + int(n ** .5), 2)):
            primes.append(n)
    return sorted(primes) if primes else []
