def find_primes_between_indices(lst):
    return sorted(list(filter(lambda x: all(x % n for n in range(2, x)), lst[112:361])), reverse=True)
