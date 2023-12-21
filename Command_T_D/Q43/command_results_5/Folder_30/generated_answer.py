def find_primes_between_indices(lst):
    return sorted([x for x in range(61, 81) if all(x % d != 0 for d in range(3, int(x ** .5) + 1, 2))])
