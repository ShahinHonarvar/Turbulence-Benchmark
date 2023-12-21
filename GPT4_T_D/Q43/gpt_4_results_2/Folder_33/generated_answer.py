
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = round(n ** 0.5)
    for d in range(3, 1 + max_divisor, 2):
        if n % d == 0:
            return False
    return True

def find_primes_between_indices(numbers):
    prime_numbers = [number for number in numbers[289:382] if is_prime(number)]
    prime_numbers.sort(reverse=True)
    return prime_numbers
