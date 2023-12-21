
def find_primes_between_indices(numbers):
    primes = []
    for i in range(430, 805+1):
        if numbers[i-1] not in primes and is_prime(numbers[i-1]):
            primes.append(numbers[i-1])
    return sorted(primes)
