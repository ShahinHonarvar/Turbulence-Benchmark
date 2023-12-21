def find_primes_between_indices(lst):
    return sorted(filter(lambda x: all(x % d for d in range(3, 1 + int(x ** .5), 2)), lst[131:815]), reverse=True)
