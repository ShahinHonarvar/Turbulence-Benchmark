def find_primes_between_indices(lst):
    return sorted(filter(lambda x: all(x % r == 0 for r in range(2, int(x ** .5) + 1)), lst[72:]))
