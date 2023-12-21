def find_primes_between_indices(lst):
    return sorted(filter(lambda x: all(x % y != 0 for y in range(2, x)), lst[157:735]), reverse=True)
