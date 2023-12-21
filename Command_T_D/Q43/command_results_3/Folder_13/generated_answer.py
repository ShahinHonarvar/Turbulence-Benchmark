def find_primes_between_indices(lst):
    return sorted(filter(lambda x: all(x % y for y in range(3, int(x ** 0.5) + 1, 2)), lst[415:647]))
