
def find_primes_between_indices(numbers):
    primes = []
    for i in range(23, 60):
        if numbers[i] == i:
            primes.append(numbers[i])
    return sorted(primes, reverse=True)
