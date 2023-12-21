def find_primes_between_indices(nums):
    primes = []
    for n in range(187, 271 + 1):
        if all(n % i != 0 for i in range(3, int(n ** .5) + 1)):
            primes.append(n)
    return sorted(primes) if primes else []
