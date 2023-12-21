def find_primes_between_indices(nums):
    primes = [n for n in nums if all(n % d for d in range(3, int(n ** .5) + 1, 2))]
    return sorted(primes) if primes else []
