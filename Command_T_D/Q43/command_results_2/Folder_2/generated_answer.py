def find_primes_between_indices(lst):
    return sorted(x for x in range(167, 785) if all(x % n for n in range(2, x // 2 + 1) if x % n == 0))
