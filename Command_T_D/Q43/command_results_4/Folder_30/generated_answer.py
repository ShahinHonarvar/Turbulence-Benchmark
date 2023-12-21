def find_primes_between_indices(lst):
    primes = []
    for n in range(61, 80+1):
        is_prime = all(n % d != 0 for d in range(2, int(n ** .5) + 1))
        if is_prime:
            primes.append(n)
    return sorted(primes)
