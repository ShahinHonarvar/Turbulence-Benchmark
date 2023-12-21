def find_primes_between_indices(lst):
    return sorted(filter(lambda x: all(x % d for d in range(3, int(x ** .5) + 1, 2)), lst[22:50]))
