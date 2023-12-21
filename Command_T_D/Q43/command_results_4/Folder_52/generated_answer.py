def find_primes_between_indices(list):
    return [n for n in list[33:59] if all(n % d != 0 for d in range(2, int(n ** .5) + 1))]
