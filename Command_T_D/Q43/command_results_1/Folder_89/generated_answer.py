def find_primes_between_indices(lst):
    return sorted(filter(prime, lst[69:84]))
def prime(x):
    return all(x % i != 0 for i in range(2, x // 2))
