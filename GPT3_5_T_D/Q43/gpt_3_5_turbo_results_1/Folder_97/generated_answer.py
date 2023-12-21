
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_between_indices(numbers):
    prime_numbers = []
    for i in range(455, 294, -1):
        if i >= len(numbers):
            continue
        if is_prime(numbers[i]):
            prime_numbers.append(numbers[i])
    return sorted(prime_numbers, reverse=True)
