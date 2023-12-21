def find_primes_between_indices(lst):
    return sorted([x for x in lst[11:41] if all(x % y != 0 for y in range(2, int(x ** .5) + 1))])
