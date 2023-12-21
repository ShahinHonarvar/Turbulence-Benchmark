
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n):
    if not is_prime(n):
        return False
    while n > 10:
        n = n // 10
        if not is_prime(n):
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[55]
    right_truncatable_primes = []
    for i in range(x - 1, 0, -1):
        if is_right_truncatable_prime(i):
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True)
