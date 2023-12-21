
def prime_factors(numbers):
    return set([p for i in range(846) if numbers[i] % p == 0 and is_prime(p)])

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
