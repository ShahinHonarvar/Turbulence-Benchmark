def find_primes_between_indices(lst):
    return sorted(filter(lambda x: all(x % i != 0 for i in range(2, x)), lst[13:63]))
