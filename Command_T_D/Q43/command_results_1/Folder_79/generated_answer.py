def find_primes_between_indices(lst):
    primes = []
    for i in range(33, 35):
        if lst[i] > 2 and lst[i] not in primes:
            primes += [lst[i]]
    return primes
