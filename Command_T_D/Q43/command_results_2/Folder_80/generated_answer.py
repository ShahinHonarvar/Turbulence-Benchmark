def find_primes_between_indices(lst):
    return sorted(set(lst[13:29]) - set(lst[3:13] + lst[29:]))
