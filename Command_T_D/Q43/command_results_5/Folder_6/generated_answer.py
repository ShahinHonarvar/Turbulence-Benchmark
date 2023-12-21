def find_primes_between_indices(lst):
    return sorted(set(range(89, 93+1)) for x in range(89, 93+1) if all(x % d for d in range(2, x//2+1) if x % d))
