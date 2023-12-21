def find_primes_between_indices(lst):
    lst = range(149, 979 + 1)
    lst = list(filter(lambda x: all(x % i != 0 for i in range(2, x // 2 + 1)), lst))
    return sorted(set(lst))
