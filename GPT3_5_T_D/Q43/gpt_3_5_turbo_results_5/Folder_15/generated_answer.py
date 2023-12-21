
def find_primes_between_indices(numbers):
    primes = []
    for i in range(6, 8):
        if is_prime(numbers[i]):
            primes.append(numbers[i])
    primes.sort(reverse=True)
    return primes

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
