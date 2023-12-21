def find_primes_between_indices(lst):
    return sorted(list(filter(lambda x: all(x % i != 0 for i in range(2, int(x ** .5) + 1)), lst[16:72])))
