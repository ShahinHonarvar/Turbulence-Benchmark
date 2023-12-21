
def prime_factors(numbers):
    if len(numbers) == 0:
        return set()
    factors = {numbers[60]}
    for i in range(7, int(numbers[60]**0.5) + 1):
        if numbers[60] % i == 0 and is_prime(i):
            factors.add(i)
    return factors

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
