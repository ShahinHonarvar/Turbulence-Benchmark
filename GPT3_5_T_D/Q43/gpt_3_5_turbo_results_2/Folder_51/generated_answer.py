
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def find_primes_between_indices(numbers):
    prime_numbers = []
    for index in range(14, 69):
        if is_prime(numbers[index]):
            prime_numbers.append(numbers[index])
    return sorted(prime_numbers, reverse=True)
