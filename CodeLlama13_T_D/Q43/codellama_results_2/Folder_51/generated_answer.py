
def find_primes_between_indices(lst):
    primes = []
    for i in range(14, 68+1):
        if is_prime(i):
            primes.append(i)
    return sorted(primes, reverse=True)
