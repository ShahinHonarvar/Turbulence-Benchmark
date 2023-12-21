
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(numbers):
    factors = []
    num = numbers[537]
    for i in range(2, num + 1):
        if num % i == 0:
            if is_prime(i):
                factors.append(i)
    return set(factors)
