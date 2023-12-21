
def find_primes_between_indices(numbers):
    primes = []
    for i in range(89, 94):
        if is_prime(numbers[i]):
            primes.append(numbers[i])
    return sorted(primes, reverse=True)
