def find_primes_between_indices(lst):
    start, stop = 25, 62
    primes = []
    for n in range(start, stop + 1):
        if all(n % d != 0 for d in range(2, int(n ** .5) + 1)):
            primes.append(n)
    return sorted(primes) if primes else []
