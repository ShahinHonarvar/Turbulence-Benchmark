def find_primes_between_indices(lst):
    primes = []
    for i in range(14, 73+1):
        if all(n % r for r in range(3, int(i**(0.5))+1)):
            primes.append(i)
    return sorted(set(primes))
