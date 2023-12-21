def find_primes_between_indices(list):
    return sorted([p for p in list if all(p % i for i in range(2, p))])
