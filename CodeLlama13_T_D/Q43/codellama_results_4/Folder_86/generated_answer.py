
def find_primes_between_indices(numbers):
    prime_numbers = []
    for i in range(459, 781):
        if is_prime(numbers[i]):
            prime_numbers.append(numbers[i])
    return sorted(prime_numbers)
