def find_primes_between_indices(lst):
    return sorted([n for n in lst[43:59] if all(n % r for r in range(2, int(n**(0.5))+1))])
