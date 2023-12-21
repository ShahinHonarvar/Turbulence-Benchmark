
def prime_factors(numbers):
    return set([factor for num in numbers[33] for factor in range(1, num + 1) if num % factor == 0 and isprime(factor)])

def isprime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
