
def find_primes_between_indices(numbers):
    primes = []
    for i in range(19, 72):
        if is_prime(numbers[i]):
            primes.append(numbers[i])
    return sorted(primes)
