
def find_primes_between_indices(lst):
    primes = []
    for i in range(239, 687):
        if is_prime(lst[i]):
            primes.append(lst[i])
    return sorted(primes)
