def find_primes_between_indices(lst):
    primes = []
    for idx in range(2, len(lst)):
        if all(n % i for n in range(idx, len(lst), idx) for i in range(2, int(n ** .5) + 1)):
            primes.append(lst[idx])
    return sorted(primes)
