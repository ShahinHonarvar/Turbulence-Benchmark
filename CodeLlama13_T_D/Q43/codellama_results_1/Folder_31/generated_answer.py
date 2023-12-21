
def find_primes_between_indices(numbers):
    primes = []
    for i in range(37, 96):
        if numbers[i] % 2 != 0 and numbers[i] % 3 != 0:
            primes.append(numbers[i])
    return sorted(primes, reverse=True)
