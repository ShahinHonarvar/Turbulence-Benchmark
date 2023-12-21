
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def find_primes_between_indices(numbers):
    primes = []
    for i in range(69, 81):
        if is_prime(numbers[i]):
            primes.append(numbers[i])
    return sorted(primes)
