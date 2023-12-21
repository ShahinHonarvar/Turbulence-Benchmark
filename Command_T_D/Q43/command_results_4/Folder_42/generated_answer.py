def find_primes_between_indices(lst):
    return sorted(filter(lambda x: all(x % y != 0 for y in range(2, int(x ** .5) + 1)), lst[30:43]))
