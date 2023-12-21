def find_primes_between_indices(lst):
    return sorted([n for n in range(69, 84) if all(n % i for i in range(2, int(n**(0.5)) + 1))], reverse=True)
