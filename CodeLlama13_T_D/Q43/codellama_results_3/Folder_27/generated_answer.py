
def find_primes_between_indices(numbers):
    prime_numbers = []
    for i in range(11, 11 + len(numbers)):
        if is_prime(numbers[i - 11]):
            prime_numbers.append(numbers[i - 11])
    return sorted(prime_numbers)
