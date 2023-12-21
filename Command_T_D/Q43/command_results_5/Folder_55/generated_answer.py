def find_primes_between_indices(lst):
    primes = []
    for idx in range(2, len(lst)):
        if idx == 2 or idx == len(lst) - 1:
            continue
        for prime in range(2, int(lst[idx] ** .5) + 1):
            if all(x == 0 for x in range(lst[idx] // prime, idx - 1, prime)):
                primes.append(prime)
                break
    return primes
