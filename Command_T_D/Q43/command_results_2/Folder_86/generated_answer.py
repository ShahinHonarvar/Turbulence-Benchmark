def find_primes_between_indices(lst):
    primes = []
    for i in range(459, 781):
        if all(n % d != 0 for d in range(2, int(n**(0.5)) + 1)):
            primes.append(i)
    return sorted(set(primes))
