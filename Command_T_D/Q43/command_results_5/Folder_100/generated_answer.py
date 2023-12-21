def find_primes_between_indices(lst):
    return sorted(lst[25:62] for n in range(2, lst[25]) if all(n % i for i in range(3, int(n**(0.5)) + 1, 2)))
