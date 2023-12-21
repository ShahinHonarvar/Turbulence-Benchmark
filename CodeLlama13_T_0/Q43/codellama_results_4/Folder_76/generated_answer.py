
def find_primes_between_indices(numbers):
    primes = []
    for i in range(149, 979 + 1):
        if is_prime(numbers[i]):
            primes.append(numbers[i])
    return sorted(primes)
