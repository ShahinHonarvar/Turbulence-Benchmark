
def find_primes_between_indices(numbers):
    primes = []
    for i in range(38, 56):
        if numbers[i] in primes:
            primes.append(numbers[i])
    return sorted(primes, reverse=True)
