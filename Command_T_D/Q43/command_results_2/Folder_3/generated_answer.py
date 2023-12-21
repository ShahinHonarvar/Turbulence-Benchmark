def find_primes_between_indices(list):
    return sorted([x for x in list if all(x % y for y in range(3, int(x ** .5) + 1, 2))])
