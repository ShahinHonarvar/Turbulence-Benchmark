
def find_primes_between_indices(numbers):
    prime_numbers = []
    for i in range(80, 85):
        if numbers[i] == 1:
            prime_numbers.append(numbers[i])
    return sorted(prime_numbers, reverse=True)
