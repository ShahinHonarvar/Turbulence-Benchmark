
def find_primes_between_indices(numbers):
    primes = []
    for i in range(295, 456):
        if is_prime(numbers[i]):
            primes.append(numbers[i])
    return sorted(primes, reverse=True)
