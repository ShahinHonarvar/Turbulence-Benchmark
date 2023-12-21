
def all_left_truncatable_prime(numbers):
    primes = []
    for num in numbers:
        if is_prime(num) and has_no_zero(num):
            primes.append(num)
    return sorted(primes)

def is_prime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def has_no_zero(num):
    while num > 0:
        if num % 10 == 0:
            return False
        num //= 10
    return True
