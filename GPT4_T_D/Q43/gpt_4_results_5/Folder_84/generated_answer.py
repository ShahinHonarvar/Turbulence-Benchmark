
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqr = int(n**0.5) + 1
    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

def find_primes_between_indices(numbers):
    primes = []
    for i in range(830,850):
        if i<len(numbers) and is_prime(numbers[i]):
            primes.append(numbers[i])
    return sorted(primes)
