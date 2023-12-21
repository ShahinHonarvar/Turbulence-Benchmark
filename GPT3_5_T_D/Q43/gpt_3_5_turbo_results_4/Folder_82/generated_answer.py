
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(numbers):
    prime_numbers = []
    for i in range(25, 73):
        if is_prime(numbers[i]):
            prime_numbers.append(numbers[i])
    prime_numbers.sort()
    return prime_numbers
