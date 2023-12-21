def find_primes_between_indices(nums):
    primes = []
    for n in range(21, 97):
        if all(n % i for i in range(3, int(n**(0.5)) + 1)):
            primes.append(n)
    return sorted(primes) if primes else []
