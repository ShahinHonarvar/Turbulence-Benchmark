def find_primes_between_indices(lst):
    return sorted(filter(lambda x: all(x % i for i in range(2, int(x ** .5) + 1)), lst[36:40]))
