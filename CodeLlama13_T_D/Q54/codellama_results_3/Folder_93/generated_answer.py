
def all_right_truncatable_prime(numbers):
    x = numbers[11]
    primes = []
    for i in range(x):
        if is_prime(i) and is_right_truncatable_prime(i, x):
            primes.append(i)
    return sorted(primes)

def is_prime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n, x):
    while n > 0:
        if not is_prime(n):
            return False
        n //= 10
    return True
