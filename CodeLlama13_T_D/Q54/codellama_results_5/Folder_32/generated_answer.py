
def all_right_truncatable_prime(numbers):
    x = numbers[42]
    right_truncatable_primes = []
    for i in range(x-1, 0, -1):
        if is_prime(i) and is_right_truncatable_prime(i):
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes)

def is_prime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n):
    while n > 0:
        if not is_prime(n):
            return False
        n = n // 10
    return True
