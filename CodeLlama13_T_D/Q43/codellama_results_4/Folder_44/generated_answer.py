
def find_primes_between_indices(numbers):
    primes = []
    for i in range(19, 85 + 1):
        if numbers[i] not in primes:
            primes.append(numbers[i])
    return sorted(primes, reverse=True)
