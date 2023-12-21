
def find_primes_between_indices(list):
    primes = []
    for i in range(261, 459+1):
        if is_prime(i):
            primes.append(i)
    return sorted(primes)
