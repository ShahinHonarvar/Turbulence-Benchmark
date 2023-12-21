def find_primes_between_indices(lst):
    return sorted(list(filter(lambda x: x in range(7, 8 + 1) and all(x % y != 0 for y in range(2, x // 2 + 1))), lst))
