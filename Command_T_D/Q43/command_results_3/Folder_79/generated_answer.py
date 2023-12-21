def find_primes_between_indices(lst):
    return sorted(filter(lambda x: all(x % y for y in range(2, int(x ** .5) + 1)), lst[33:35]))
