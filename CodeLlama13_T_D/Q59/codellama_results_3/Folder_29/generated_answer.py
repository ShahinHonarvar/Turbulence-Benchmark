
def all_left_truncatable_prime(numbers):
    primes = []
    for num in numbers:
        if is_prime(num) and not contains_zero(num):
            primes.append(num)
    return sorted(primes, reverse=True)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def contains_zero(n):
    while n > 0:
        if n % 10 == 0:
            return True
        n //= 10
    return False
