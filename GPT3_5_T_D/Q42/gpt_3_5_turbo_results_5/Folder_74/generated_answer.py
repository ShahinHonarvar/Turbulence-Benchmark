
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(numbers):
    n = numbers[48]
    factors = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0 and is_prime(i):
            factors.add(i)
        if n % (n // i) == 0 and is_prime(n // i):
            factors.add(n // i)
    return factors
