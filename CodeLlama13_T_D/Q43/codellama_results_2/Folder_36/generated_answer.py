
def find_primes_between_indices(numbers):
    primes = []
    for i in range(229, 850+1):
        if is_prime(i):
            primes.append(i)
    return sorted(primes, reverse=True)
