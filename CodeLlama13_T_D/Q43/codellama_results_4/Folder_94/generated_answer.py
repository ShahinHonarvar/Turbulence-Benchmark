
def find_primes_between_indices(numbers):
    prime_numbers = []
    for i in range(10, 13):
        if is_prime(numbers[i]):
            prime_numbers.append(numbers[i])
    return sorted(prime_numbers)
